import os,sys
from datetime import datetime

# create artifact ->create pipeline folder with time stamp so that we can handle error easily so we make function to do this se below->we store all outputs in artifact folder

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP=get_current_time_stamp()

#We can do direct dataset path but here we do using code see below
ROOT_DIR_KEY=os.getcwd()
DATA_DIR='Data'
DATA_DIR_KEY='finalTrain.csv'

ARTIFACT_DIR_KEY='Artifact'

#data ingestion related variables
DATA_INGESTION_KEY='data_ingestion'

DATA_INGESTION_RAW_DATA_DIR='raw_data_dir'#store here downloaded data 
DATA_INGESTION_INGESTED_DATA_DIR_KEY='ingested_dir'#here we split & store data into train and test

RAW_DATA_DIR_KEY='raw.csv'#this file will store in raw_data_dir folder
TRAIN_DATA_DIR_KEY='train.csv'
TEST_DATA_DIR_KEY='test.csv'



# Now We define Data Transformation related variables
# artifact/data_transformation/processor->processor.pkl and transformation->train.csv and test.csv

DATA_TRANSFORMATION_ARTIFACT="data_transformation"
DATA_PREPROCEED_DIR='processor'
DATA_TRANSFORMATION_PROCESSING_OBJ='processor.pkl'
DATA_TRANSFORM_DIR='transformation'
TRANSFORM_TRAIN_DIR_KEY='train.csv'
TRANSFORM_TEST_DIR_KEY='test.csv'