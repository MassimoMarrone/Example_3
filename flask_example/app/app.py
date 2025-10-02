from flask import Flask, render_template, request
from flask_restful import Api
from resources.forecast import ForecastHandler, Forecaster
import logging
import json

app = Flask(__name__)
api = Api(app)

forecaster = Forecaster()
api.add_resource(ForecastHandler, '/forecast', resource_class_kwargs={'forecaster': forecaster})

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/forecast_web', methods=['POST'])
def forecast_web():
    store_number = int(request.form.get('store_number'))
    forecast_start_date = request.form.get('forecast_start_date')
    # chiamiamo il metodo forecast passando i parametri
    result = forecaster.forecast(params={"store_number": store_number, "forecast_start_date": forecast_start_date})
    return render_template('index.html', forecast=result)

if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.INFO,
                        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    logging.info('Main app sequence begun')
    app.run(debug=True, host='0.0.0.0', port=5000)
    logging.info('App finished')
