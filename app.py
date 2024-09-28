from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.pipelines.training_pipeline import TrainingPipeline
from src.MLPROJECT.pipelines.prediction_pipeline import PredictionPipeline, CustomData
import sys

if __name__=='__main__':
    logging.info('The Execution has started')
    
    try:
        # training_pipeline = TrainingPipeline()
        # training_pipeline.initiate_training_pipeline()

        age = int(input('age:'))
        studytime = int(input('studytime:'))
        input_data=CustomData(
            age=age,
            studytime=studytime
        )
        input_features_df=input_data.get_data_as_data_frame()

        prediction_pipeline=PredictionPipeline()
        results=prediction_pipeline.predict(input_features_df)
        print(f'Results:{results}')

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)