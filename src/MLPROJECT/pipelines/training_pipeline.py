from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.MLPROJECT.components.data_transformation import DataTransformation,DataTransformationConfig
from src.MLPROJECT.components.model_trainer import ModelTrainer, ModelTrainerConfig
import sys

class TrainingPipeline:
    def __init__(self):
        pass

    def initiate_training_pipeline(self):
        logging.info('The Training Pipeline has started')
        
        try:
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    
            data_transformation = DataTransformation()
            transformed_train_data, transformed_test_data = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
    
            model_trainer = ModelTrainer()
            trained_model_path = model_trainer.initiate_model_training(transformed_train_data, transformed_test_data)
            logging.info('The Training Pipeline has executed successfully')
    
        except Exception as e:
            logging.info("Custom Exception")
            raise CustomException(e, sys)