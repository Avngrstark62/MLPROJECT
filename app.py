from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.pipelines.training_pipeline import TrainingPipeline
import sys

if __name__=='__main__':
    logging.info('The Execution has started')
    
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.initiate_training_pipeline()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)