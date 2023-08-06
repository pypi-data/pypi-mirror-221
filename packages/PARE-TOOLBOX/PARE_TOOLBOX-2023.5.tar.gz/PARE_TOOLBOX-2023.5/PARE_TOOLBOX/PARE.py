import numpy as np
import random
import pandas as pd
import json
import time
from datetime import datetime
from scipy.stats.distributions import norm
from scipy.stats.distributions import gumbel_r
from scipy.stats.distributions import gumbel_l
from scipy.stats.distributions import lognorm
from scipy.stats.distributions import uniform
from scipy.stats.distributions import triang
import multiprocessing
from multiprocessing import Pool
import PARE_TOOLBOX.ZIPPER as z


def SAMPLING(**kwargs):
    """ 
    This algorithm generates a set of random numbers according to a type distribution.

    See documentation in wmpjrufg.github.io/RASDPY/
    """
    if len(kwargs) != 4:
        raise ValueError("this fuction require four inputs!")

    # Creating variables
    N_POP = kwargs['N_POP']
    D = kwargs['D']
    MODEL = kwargs['MODEL']
    VARS = kwargs['VARS']
    RANDOM_STATE = random.sample(range(1, 1000), D)
    RANDOM_SAMPLING = np.zeros((N_POP, D))
    
    # Monte Carlo sampling
    if MODEL.upper() == 'MCS':
        for I in range(D):
            # Type of distribution, mean and standard deviation
            TYPE = VARS[I][0].upper()
            MEAN = VARS[I][1]
            STD = VARS[I][2]
            # Normal or Gaussian
            if TYPE == 'GAUSSIAN' or TYPE == 'NORMAL':
                RANDOM_SAMPLING[:, I] = norm.rvs(loc = MEAN, scale = STD, size = N_POP, random_state = RANDOM_STATE[I])
            # Gumbel right or Gumbel maximum
            elif TYPE == 'GUMBEL MAX':
                RANDOM_SAMPLING[:, I] = gumbel_r.rvs(loc = MEAN, scale = STD, size = N_POP, random_state = RANDOM_STATE[I])
            # Gumbel left or Gumbel minimum
            elif TYPE == 'GUMBEL MIN':
                RANDOM_SAMPLING[:, I] = gumbel_l.rvs(loc = MEAN, scale = STD, size = N_POP, random_state = RANDOM_STATE[I])
            # Lognormal
            elif TYPE == 'LOGNORMAL':
                RANDOM_SAMPLING[:, I] = lognorm.rvs(s = STD, loc = MEAN, scale = np.exp(MEAN), size = N_POP, random_state = RANDOM_STATE[I])
            # Uniform
            elif TYPE == 'UNIFORM':
                RANDOM_SAMPLING[:, I] = uniform.rvs(loc = MEAN, scale=STD, size = N_POP, random_state = RANDOM_STATE[I])
            # Triangular
            elif TYPE == 'TRIANGULAR':
                LOC = VARS[I][1]
                SCALE = VARS[I][2]
                C = VARS[I][3]
                #loc is the start, scale is the base width, c is the mode percentage
                RANDOM_SAMPLING[:, I] = triang.rvs(loc = LOC, scale = SCALE, c = (C - LOC) / (SCALE - LOC), size = N_POP, random_state = RANDOM_STATE[I])

    return RANDOM_SAMPLING, RANDOM_STATE

def EVALUATION_MODEL(INFO):
    SAMPLE = INFO[0]
    OF_FUNCTION = INFO[1]
    NULL_DIC = INFO[2]
    R, S, G = OF_FUNCTION(SAMPLE, NULL_DIC)
    RESULTS = [R, S, G]
    return RESULTS

def MCS_LHS_ALGORITHM(SETUP, OF_FUNCTION):
    """
    This function creates the samples and evaluates the limit state functions.
    
    See documentation in wmpjrufg.github.io/RASDPY/
    """ 
    
    # Initial setup
    INIT = time.time()
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    MODEL = SETUP['MODEL']
    VARS = SETUP['VARS']
    N_G = SETUP['N_G']
    STEP = 1000
    NULL_DIC = SETUP['NULL_DIC']
    RESULTS_R = np.zeros((N_POP, N_G))
    RESULTS_S = np.zeros((N_POP, N_G))
    RESULTS_G = np.zeros((N_POP, N_G))
    RESULTS_I = np.zeros((N_POP, N_G))  
    MODEL_NAME = 'MCS_LHS'
    TYPE_PROCESS = 'PARALLEL'
    
    # BETA_DF = RASD_CL.PROBABILITY_OF_FAILURE() - Vamos mudar esse calc aqui para uma derivada numérica vou pensar em como fazer

    # Creating samples   
    DATASET_X, RANDOM_STATE = SAMPLING(N_POP = N_POP, D = D, MODEL = MODEL, VARS = VARS)   

    # Multiprocess Objective Function evaluation
    if TYPE_PROCESS == 'PARALLEL':
        POOLS = multiprocessing.cpu_count() - 1   
        INFO = [[list(I), OF_FUNCTION, NULL_DIC] for I in DATASET_X]
        with Pool(processes = POOLS) as pool:
            RESULT = pool.map_async(EVALUATION_MODEL, INFO)
            RESULT = RESULT.get()
        for K in range(N_POP):
            RESULTS_R[K, :] = RESULT[K][0]
            RESULTS_S[K, :] = RESULT[K][1]
            RESULTS_G[K, :] = RESULT[K][2]
            RESULTS_I[K, :] = [0 if value <= 0 else 1 for value in RESULT[K][2]]
    # Singleprocess Objective Function evaluation
    elif TYPE_PROCESS == 'SERIAL':
        RESULT = []
        for I in DATASET_X:
            INFO = [I, OF_FUNCTION, NULL_DIC]
            RES = EVALUATION_MODEL(INFO)
            RESULT.append(RES)
        for K in range(N_POP):
            RESULTS_R[K, :] = RESULT[K][0]
            RESULTS_S[K, :] = RESULT[K][1]
            RESULTS_G[K, :] = RESULT[K][2]
            RESULTS_I[K, :] = [0 if value <= 0 else 1 for value in RESULT[K][2]] 
            
    # Storage all results
    AUX = np.hstack((DATASET_X, RESULTS_R, RESULTS_S, RESULTS_G, RESULTS_I))
    RESULTS_RASD = pd.DataFrame(AUX)          
    # Rename columns in dataframe 
    COLUMNS_NAMES = []
    for L in range(D):
        COLUMNS_NAMES.append('X_' + str(L))
    for L in range(N_G):
        COLUMNS_NAMES.append('R_' + str(L))  
    for L in range(N_G):
        COLUMNS_NAMES.append('S_' + str(L))
    for L in range(N_G):
        COLUMNS_NAMES.append('G_' + str(L))
    for L in range(N_G):
        COLUMNS_NAMES.append('I_' + str(L))
    RESULTS_RASD.columns = COLUMNS_NAMES
    
    # Resume data 
    # Creates data for .json type output considering the chosen step
    VALUES = list(np.arange(1, N_POP, STEP, dtype = int))
    if VALUES[-1] != N_POP:
        VALUES.append(N_POP)
    VALUES = [int(X) for X in VALUES]
    RESUME_DATA = {'seeds': RANDOM_STATE, 'number of samples': VALUES, 'results': {}}
    for L in range(N_G):
        KEY = f'I_{L}' 
        N_F = []
        P_F = []
        for I in VALUES:
            LINES = RESULTS_RASD[:I]
            # Failure probability
            N_FAILURE = int(LINES[KEY].sum())
            P_FVALUE = N_FAILURE / I
            N_F.append(N_FAILURE)
            P_F.append(P_FVALUE)
        RESUME_DATA['results'][KEY] = {'NF': N_F, 'PF': P_F}

    # Resume process (Time and outputs)
    END = time.time()
    # Emoji unicode: https://apps.timwhitlock.info/emoji/tables/unicode
    print('PAREpy report: \n') 
    NAME = MODEL_NAME + '_' + str(datetime.now().strftime('%Y%m%d-%H%M%S'))
    print(f' \U00003299 ID report: {NAME} \n') 
    print(' \U0001F680' + f' Process Time {TYPE_PROCESS} version ' + '\U000023F0' + ' %.2f' % (END - INIT), 'Seconds \n') 
    with open(NAME + '.json', 'w') as FILE:
        json.dump(RESUME_DATA, FILE)  
        print(' \U0001F197' + ' Save results in .json file! \n')
    RESULTS_RASD.to_csv(NAME + '.txt', sep = '\t', index = False)
    print(' \U0001F197' + ' Save dataset in .txt file!')
    z.ZIPPER(NAME)
    z.UNZIPPER(NAME)
    print('\n \U0001F4C1' + ' Files into the folder' +  ' ' + NAME) 

    """
    BETA_DF = pd.read_csv('RASD_TOOLBOX/beta_df.txt', delimiter = ";",  names = ['PF' ,'BETA'])
    BETA_APROX = round(P_FVALUE,5)
    BETA_VALUE_INDEX = (BETA_DF['PF'].sub(P_FVALUE).abs().idxmin())
    BETA_VALUE = BETA_DF['BETA'][BETA_VALUE_INDEX]   
    BETA_F.append(BETA_VALUE)

    # Save results
    RESULTS_REP = {'TOTAL RESULTS': RESULTS_RASD, 'NUMBER OF FAILURES': N_F, 'PROBABILITY OF FAILURE': P_F, 'BETA INDEX': BETA_F}
    RESULTS.append(RESULTS_REP)
    NAME = 'RASD_' + MODEL + '_REP_' + str(J) + '_SAMPLES_' + str(N_POP) + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S')) + '.txt'
    HEADER_NAMES =  ';'.join(COLUMNS_NAMES)
    np.savetxt(NAME, RESULTS_RASD, fmt = '%1.5f', delimiter = ';' , header = HEADER_NAMES)
    """
    return RESULTS_RASD