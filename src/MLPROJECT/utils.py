import os
import sys
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
        query = "SELECT * FROM chapter_progress;"
        df = pd.read_sql(query, engine)
        return df

    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e, sys)