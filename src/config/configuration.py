import os, sys
from src.constants import *

ROOT_DIR = ROOT_DIR_KEY

#dataset url
DATASET_PATH = os.path.join(ROOT_DIR,DATA_DIR,DATA_DIR_KEY)#Data folder available in pro. folder
#OR we can give direct path copy from local but if we give this code to someone may be their path
#will be different so this is not good practise


RAW_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_KEY,CURRENT_TIME_STAMP,
                            DATA_INGESTION_RAW_DATA_DIR_KEY,RAW_DATA_DIR_KEY)


TRAIN_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_KEY,CURRENT_TIME_STAMP,
                            DATA_INGESTION_INGESTED_DIR_NAME_KEY,TRAIN_DATA_DIR_KEY)

TEST_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_KEY,CURRENT_TIME_STAMP,
                            DATA_INGESTION_INGESTED_DIR_NAME_KEY,TEST_DATA_DIR_KEY)




# Data Transformation steps
PREPROCESSING_OBJ_FILE = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_ARTIFACT,
                                    DATA_PREPROCESSED_DIR,DATA_TRANSFORMATION_PREPROCESSING_OBJ)

TRANSFORMED_TRAIN_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_ARTIFACT,
                                        DATA_TRANSFORMED_DIR,TRANSFORMED_TRAIN_DIR_KEY)

TRANSFORMED_TEST_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_ARTIFACT,
                                        DATA_TRANSFORMED_DIR,TRANSFORMED_TEST_DIR_KEY)

FEATURE_ENGG_OBJ_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_ARTIFACT,
                                        DATA_PREPROCESSED_DIR,'feature_engg.pkl')


# Model Training
MODEL_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,MODEL_TRAINER_KEY,MODEL_OBJECT)
