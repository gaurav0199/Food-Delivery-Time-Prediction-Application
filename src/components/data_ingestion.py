from src.components import *
# from src.components import DataTransformation
from src.config.configuration import *


import os,sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path:str = TRAIN_FILE_PATH
    test_data_path:str = TEST_FILE_PATH
    raw_data_path:str = RAW_FILE_PATH

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def inititate_data_ingestion(self):
        # we write complete code in try and except block so that we can capture errors
        try:
            df=pd.read_csv(DATASET_PATH)

            # df=pd.read_csv(os.path.join(complete dataset path direct method ))
            
            #make artifact directory if exist_ok skip this step
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)

            #save data
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False)

            #split data
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)

            # make folder for train data
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.train_data_path,header=True)
            
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,header=True)
            
            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)


# for testing purpose # Data Ingestion
# if __name__=="__main__":
#     obj=DataIngestion()
#     train_data,test_data=obj.inititate_data_ingestion()


#Data Transformation
# if __name__ == "__main__":
#    obj = DataIngestion()
#    train_data, test_data = obj.inititate_data_ingestion()

#    data_transformation=DataTransformation()
#    train_arr, test_arr,_ = data_transformation.inititate_data_transformation(train_data, test_data)



# Model Trainging
if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path,test_data_path=obj.inititate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.inititate_data_transformation(train_data_path,test_data_path)

    model_trainer=ModelTrainer()
    print(model_trainer.inititate_model_traing(train_arr,test_arr))