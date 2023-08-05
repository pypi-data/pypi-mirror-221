import shutil
import os.path
import json


def LIST_ALL_FILES(PATH = './'):
    return os.listdir(PATH) 

def FOLDER_CREATOR(NAME, PATH='./'):
    """
    You can insert the file name with extension or without extension, don't need the path (The path is the current directory).
    """
    
    if '.json' in NAME or '.txt' in NAME:
        NAME = NAME.split('.')[0]  
    FOLDER_NAME = NAME
    os.mkdir(FOLDER_NAME)

    return PATH + FOLDER_NAME


def FOLDER_MOVER(NAME, PATH='./'):
    """
    You can insert the file name with extension or without extension, don't need the path (The path is the current directory).
    """
    
    if '.json' in NAME or '.txt' in NAME:
        NAME = NAME.split('.')[0]
    FOLDER_NAME = NAME
    TXT_FILE = NAME + '.txt'
    JSON_FILE = NAME + '.json'
    
    shutil.move(TXT_FILE, PATH + FOLDER_NAME)
    shutil.move(JSON_FILE, PATH + FOLDER_NAME)

    return PATH + FOLDER_NAME


def FOLDER_REMOVER(NAME, PATH='./'):
    if '.json' in NAME or '.txt' in NAME:
        NAME = NAME.split('.')[0]
    
    shutil.rmtree(NAME)
    return PATH + NAME


def ZIPPER(NAME, PATH = './'):
    """
    You can insert the file name with extension or without extension, don't need the path (zipping on the root directory).
    """
    
    FOLDER_CREATOR(NAME)
    FOLDER_MOVER(NAME)

    if '.json' in NAME or '.txt' in NAME:
        NAME = NAME.split('.')[0]
    
    ZIP_NAME = PATH + NAME
    shutil.make_archive(ZIP_NAME, 'zip', root_dir = PATH, base_dir=ZIP_NAME, verbose=0, dry_run=False, owner=None, group=None, logger=None)
    FOLDER_REMOVER(NAME)
    print('\n \U0001F197'+' Zip file created: ', ZIP_NAME)
    
    return PATH + ZIP_NAME
    

def UNZIPPER(NAME, PATH = './'):
    """
    You can insert the file name with extension or without extension, don't need the path (unzipping on the root directory).
    """
    if not 'zip' in NAME:
        NAME = NAME + '.zip'

    shutil.unpack_archive(NAME, PATH, 'zip')

def READ_MCS_LHS_FOLDERS(PATH='./'):
    FILES = os.listdir(PATH)
    FOLDERS = []
    for FILE in FILES:
        if 'MCS_LHS' in FILE and not '.zip' in FILE:
            FOLDERS.append(FILE)
    
    return FOLDERS


def CONCAT_RESULTS(PATH = './'):
    
    FOLDERS = READ_MCS_LHS_FOLDERS(PATH)
    PRINT_TITLE = True

    for FOLDER in FOLDERS:
        
        FILES = os.listdir(PATH+FOLDER)
        JSON_FILE = [FILE for FILE in FILES if '.json' in FILE][0]
        TXT_FILE = [FILE for FILE in FILES if '.txt' in FILE][0]    
        
        with open(PATH+FOLDER+'/'+TXT_FILE) as F:
            TXT_DATA = F.readlines()
            
            with open(PATH + 'concat_result.txt', 'a') as F:
                if(PRINT_TITLE):
                    F.writelines(TXT_DATA)
                    PRINT_TITLE = False
                else:
                    TXT_DATA = TXT_DATA[1:]
                    F.writelines(TXT_DATA)