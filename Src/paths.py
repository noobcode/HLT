import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) #this file's path
ROOT_DIR = os.path.dirname(FILE_PATH) #Project root dir - '.../HLT'

DrugBank_DIR_train = os.path.join(ROOT_DIR, 'Train', 'DrugBank')
MedLine_DIR_train = os.path.join(ROOT_DIR, 'Train', 'MedLine')
DrugBank_DIR_test1 = os.path.join(ROOT_DIR, 'Test', 'Task1', 'DrugBank')
MedLine_DIR_test1 = os.path.join(ROOT_DIR, 'Test', 'Task1', 'MedLine')
DrugBank_DIR_test2 = os.path.join(ROOT_DIR, 'Test', 'Task2', 'DrugBank')
MedLine_DIR_test2 = os.path.join(ROOT_DIR, 'Test', 'Task2', 'MedLine')

TRAIN_DIRS = [DrugBank_DIR_train, MedLine_DIR_train]
TEST1_DIRS = [DrugBank_DIR_test1, MedLine_DIR_test1]
TEST2_DIRS = [DrugBank_DIR_test2, MedLine_DIR_test2]
TEST_DIRS = TEST1_DIRS + TEST2_DIRS
DATA_DIRS = [TRAIN_DIRS, TEST1_DIRS, TEST2_DIRS]


SENTENCE_PATH_train = os.path.join(ROOT_DIR, "Train", "sentences.csv")
ENTITY_PATH_train = os.path.join(ROOT_DIR, "Train", "entities.csv")
PAIR_PATH_train = os.path.join(ROOT_DIR, "Train", "pairs.csv")

SENTENCE_PATH_test1 = os.path.join(ROOT_DIR,"Test","Task1", "sentences.csv")
ENTITY_PATH_test1 = os.path.join(ROOT_DIR, "Test", "Task1", "entities.csv")
PAIR_PATH_test1 = os.path.join(ROOT_DIR, "Test", "Task1", "pairs.csv")


SENTENCE_PATH_test2 = os.path.join(ROOT_DIR, "Test", "Task2", "sentences.csv")
ENTITY_PATH_test2 = os.path.join(ROOT_DIR, "Test", "Task2", "entities.csv")
PAIR_PATH_test2 = os.path.join(ROOT_DIR, "Test", "Task2", "pairs.csv")

# Check directory paths
#print(ROOT_DIR)
#print(DrugBank_DIR_train, MedLine_DIR_train)

