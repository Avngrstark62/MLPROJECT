import numpy as np
import pandas as pd
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.logger import logging
from src.MLPROJECT.utils import save_obj_file
import os
import sys
import pickle
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    transformed_train_data_path = os.path.join('artifacts', 'transformed_train_data.pkl')
    transformed_test_data_path = os.path.join('artifacts', 'transformed_test_data.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def initiate_data_transformation(self, train_data_path, test_data_path):
        try:
            logging.info('Reading train and test data')
            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)

            logging.info('Transforming train and test data')
            transformed_train_data = train_data[['age', 'studytime', 'G3']]
            transformed_test_data = test_data[['age', 'studytime', 'G3']]

            logging.info('Saving transformed train and test data')
            transformed_train_data_path = self.data_transformation_config.transformed_train_data_path
            transformed_test_data_path = self.data_transformation_config.transformed_test_data_path
            save_obj_file(transformed_train_data, transformed_train_data_path)
            save_obj_file(transformed_test_data, transformed_test_data_path)

            logging.info('Data Transformation is complete')
            return transformed_train_data, transformed_test_data
        
        except Exception as e:
            logging.info('Custom Exception')
            raise CustomException(e, sys)