from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os,sys
from src.config.configuration import *

from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import DataIngestion

class Train:
    def __init__(self):
        self.c=0 #initialize an instance variable 'c' with the value 0
        print(f"************{self.c}******************")

    def main(self):
        obj = DataIngestion()
        train_data_path,test_data_path=obj.inititate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr,test_arr,_ = data_transformation.inititate_data_transformation(train_data_path,test_data_path)

        model_trainer = ModelTrainer()
        model_trainer.inititate_model_traing(train_arr,test_arr)