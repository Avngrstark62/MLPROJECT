import os
import sys
import pickle
from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
DATABASE_URL = os.getenv('POSTGRES_DATABASE_URL')
engine = create_engine(DATABASE_URL)


def read_sql_data():
    logging.info('Reading SQL data from database')
    try:
        engine = create_engine(DATABASE_URL)
        logging.info('Connected to Database')
        query = "SELECT * FROM student_performance_data;"
        df = pd.read_sql(query, engine)
        return df

    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e, sys)
    

def save_obj_file(obj, file_path):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    
    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)