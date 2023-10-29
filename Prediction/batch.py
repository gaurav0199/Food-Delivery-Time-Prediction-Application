from src.constants import *
from src.config.configuration import *
import os,sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
import pickle
from src.utils import load_model
from sklearn.pipeline import Pipeline

PREDICTION_FOLDER='batch_prediction'
PREDICTION_CSV="prediction_csv"
PREDICTION_FILE='prediction.csv'

FEATURE_ENG_FOLDER="feature_eng"

ROOT_DIR=os.getcwd()
FEATURE_ENG=os.path.join(ROOT_DIR,PREDICTION_FOLDER,FEATURE_ENG_FOLDER)
BATCH_PREDICTION=os.path.join(ROOT_DIR,PREDICTION_FOLDER,PREDICTION_CSV)


class Batch_prediction:
    def __init__(self,input_file_path,
                    model_file_path,
                    transformer_file_path,
                    feature_engineering_file_path) -> None:
        
        self.input_file_path = input_file_path
        self.model_file_path = model_file_path
        self.transformer_file_path = transformer_file_path
        self.feature_engineering_file_path = feature_engineering_file_path

    
    def start_batch_prediction(self):
        try:
            logging.info("Loading the saved pipeline")

            #Load the feature engineering pipeline path
            with open(self.feature_engineering_file_path,'rb') as f:
                feature_pipeline = pickle.load(f)
            logging.info(f"Feature eng object accessed :{self.feature_engineering_file_path}")
            
            #Load the data transformation pipeline path
            with open(self.transformer_file_path,'rb') as f:
                preprocessor = pickle.load(f)
            logging.info(f"Preprocessor Object accessed :{self.transformer_file_path}")
            
            #Load the model separatly
            model = load_model(file_path=self.model_file_path)

            logging.info(f"Model file path :{self.model_file_path}")

            #Create a feature engineering pipeline
            feature_engineering_pipeline=Pipeline([
                ('feature_engineering',feature_pipeline)
            ])

            #Read the input file
            df = pd.read_csv(self.input_file_path)

            df.to_csv('df_zomato_delivery_time_prediction.csv')#save data

            #Apply Feature engineering pipeline steps
            df = feature_engineering_pipeline.transform(df)

            df.to_csv('feature_engineering.csv')

            #Save the feature-engineered data as a csv file
            FEATURE_ENGINEERING_PATH = FEATURE_ENG
            os.makedirs(FEATURE_ENGINEERING_PATH, exist_ok=True)

            file_path = os.path.join(FEATURE_ENGINEERING_PATH,'batch_feature_eng.csv')

            df.to_csv(file_path, index=False)
            logging.info("Feature-engineered batch data save as csv")

            #Dropping target column
            df=df.drop('Time_taken (min)', axis=1)
            df.to_csv('dropped_Time_taken_min.csv')


            logging.info(f"Coliumn before transformation: {', '.join(f'{col}: {df[col].dtype}' for col in df.columns)}")
           
            #Transform the feature-engineered data using the preprocessor
            transformed_data = preprocessor.transform(df)
            logging.info(f"Transformed Data Shape: {transformed_data.shape}")

            logging.info(f"Loaded numpy from batch prediction: {transformed_data}")
            file_path = os.path.join(FEATURE_ENGINEERING_PATH, 'preprocessor.csv')

            logging.info(f"Model Data Type: {type(model)}")

            predictions = model.predict(transformed_data)
            logging.info(f"Predictions done: {predictions}")

            #Create a Dataframe from the predictions array
            df_predictions = pd.DataFrame(predictions, columns=['prediction'])

            #Save the predictions to a csv file 
            BATCH_PREDICTION_PATH = BATCH_PREDICTION
            os.makedirs(BATCH_PREDICTION_PATH,exist_ok=True)
            csv_path = os.path.join(BATCH_PREDICTION_PATH,'prediction.csv')

            df_predictions.to_csv(csv_path, index=False)
            logging.info(f"Batch predictions save to '{csv_path}'.")



        except Exception as e:
            CustomException(e,sys)