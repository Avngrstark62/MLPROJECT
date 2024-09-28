import pandas as pd
from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.utils import load_object
import os
import sys

class PredictionPipeline:
    def __init__(self):
        pass

    def preprocess_input_features(self, input_features):
        processed_input_features = input_features
        return processed_input_features

    def predict(self, input_features):
        logging.info('The Prediction Pipeline has started')
        try:
            processed_input_features = self.preprocess_input_features(input_features)
            model_path = os.path.join("artifacts","trained_model.pkl")
            model=load_object(file_path=model_path)
            results = model.predict(processed_input_features)
            logging.info('The Prediction Pipeline has executed successfully')

            return results
    
        except Exception as e:
            logging.info("Custom Exception")
            raise CustomException(e, sys)

class CustomData:
    def __init__(  self,
        age: int,
        studytime: int):

        self.age = age
        self.studytime = studytime

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "studytime": [self.studytime]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)