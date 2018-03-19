import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) #this file's path
ROOT_DIR = os.path.dirname(FILE_PATH) #Project root dir - '.../HLT'

DrugBank_DIR_train = os.path.join(ROOT_DIR, 'Train', 'DrugBank')
MedLine_DIR_train = os.path.join(ROOT_DIR, 'Train', 'MedLine')
DATA_DIRS = [DrugBank_DIR_train, MedLine_DIR_train]

SENTENCE_PATH = os.path.join(ROOT_DIR, "Train", "sentences.csv")
ENTITY_PATH = os.path.join(ROOT_DIR, "Train", "entities.csv")

# Check directory paths
#print(ROOT_DIR)
#print(DrugBank_DIR_train, MedLine_DIR_train)

