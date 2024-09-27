from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.MLPROJECT.components.data_transformation import DataTransformation,DataTransformationConfig
import sys

if __name__=='__main__':
    logging.info('The Execution has started')
    
    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        pass

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)