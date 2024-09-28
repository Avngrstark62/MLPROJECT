from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.pipelines.prediction_pipeline import PredictionPipeline, CustomData
import sys
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    studytime = int(request.form['studytime'])

    input_data=CustomData(
        age=age,
        studytime=studytime
    )
    input_features_df=input_data.get_data_as_data_frame()

    prediction_pipeline=PredictionPipeline()
    results=prediction_pipeline.predict(input_features_df)
    return render_template('index.html', prediction_text=f'Predicted Grade: {results[0]}')

if __name__=='__main__':
    try:
        app.run(debug=True)
        logging.info('The app is running')
    
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)