import numpy as np
import pandas as pd
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.logger import logging
from src.MLPROJECT.utils import save_obj_file
import os
import sys
import pickle
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts/trained_model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_training(self, train_data, test_data):
        try:
            logging.info('Model Training Started')
            X_train = train_data.drop('G3', axis=1)
            Y_train = train_data['G3']
            X_test = test_data.drop('G3', axis=1)
            Y_test = test_data['G3']

            model = LinearRegression()
            model.fit(X_train, Y_train)
            Y_pred = model.predict(X_test)
            model_r2_score = r2_score(Y_pred, Y_test)
            logging.info('Model Training Finished')
            logging.info(f'R2_score of the Trained Model is {model_r2_score}')

            model_path = self.model_trainer_config.trained_model_file_path
            save_obj_file(model, model_path)
            logging.info('Trained Model Saved')

            return model_path
        
        except Exception as e:
            logging.info('Custom Exception')
            raise CustomException(e, sys)