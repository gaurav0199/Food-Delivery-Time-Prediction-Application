import os,sys
from datetime import datetime

# create artifact ->create pipeline folder with time stamp so that we can handle error easily so we make function to do this se below->we store all outputs in artifact folder

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

#We can put direct dataset path but here we do using code(create variable) 
ROOT_DIR_KEY = os.getcwd()

DATA_DIR = 'Data'
DATA_DIR_KEY = 'finalTrain.csv'

ARTIFACT_DIR_KEY = 'Artifact'

#data ingestion related variables
DATA_INGESTION_KEY = 'data_ingestion'

DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'#store here downloaded data 
DATA_INGESTION_INGESTED_DIR_NAME_KEY = 'ingested_dir'#here we split & store data into train and test

RAW_DATA_DIR_KEY = 'raw.csv'#this file will store in raw_data_dir folder
TRAIN_DATA_DIR_KEY = 'train.csv'
TEST_DATA_DIR_KEY = 'test.csv'

# data validation

DATA_VALIDATION_KEY = 'data_validation'

DATA_VALIDATION_VALIDATED_DIR_KEY = 'validated_dir'
VALIDATED_TRAIN_DIR_KEY = 'validated_train.csv'
VALIDATED_TEST_DIR_KEY = 'validated_test.csv'


# Now We define Data Transformation related variables
# artifact/data_transformation/processor->processor.pkl and transformation->train.csv and test.csv

DATA_TRANSFORMATION_ARTIFACT = "data_transformation"

DATA_PREPROCESSED_DIR = 'preprocessed'
DATA_TRANSFORMATION_PREPROCESSING_OBJ = 'preprocessor.pkl'

DATA_TRANSFORMED_DIR = 'transformed_data'
TRANSFORMED_TRAIN_DIR_KEY = 'train.csv'
TRANSFORMED_TEST_DIR_KEY = 'test.csv'




# Model Training
MODEL_TRAINER_KEY = 'model_trainer'
MODEL_OBJECT = 'model.pkl'