import requests
from flask import Flask
from flask import jsonify
import os
import db.db as db
import utils
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_BASE_URL = os.getenv('API_BASE_URL')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Forecast python project.'

@app.route('/forecast')
def forecast():
    response = requests.get('{}?&units=metric&lat=-12.9704&lon=-38.5124&appid={}'.format(API_BASE_URL, API_KEY))
    err = utils.save_DB(response)
    if  err:
        return "An unexcpeted error ocurred", 500

    return jsonify(response.json()), 200

@app.route('/forecast/<lat>/<lon>')
def forecastByCoordinates(lat, lon):
    response = requests.get('{}?&units=metric&lat={}&lon={}&appid={}'.format(API_BASE_URL, lat, lon, API_KEY))
    err = utils.save_DB(response)
    if  err:
        return "An unexcpeted error ocurred", 500    
    return jsonify(response.json()), 200

@app.route('/forecast/minimal')
def forecastMinimal():
    response = requests.get('{}?&units=metric&lat=-12.9704&lon=-38.5124&appid={}'.format(API_BASE_URL, API_KEY))
    consults, err = utils.save_DB_minimal(response)
    if err:
        return "An unexcpeted error ocurred", 500
    return consults, 200

@app.route('/forecast/minimal/<lat>/<lon>')
def forecastMinimalByCoordinates(lat, lon):
    response = requests.get('{}?&units=metric&lat={}&lon={}&appid={}'.format(API_BASE_URL, lat, lon, API_KEY))
    consults, err = utils.save_DB_minimal(response)
    if  err:
        return "An unexcpeted error ocurred", 500
    return consults, 200

@app.route('/consults')
def getConsults():
    data, err = db.getConsults()
    if  err:
        return "An unexcpeted error ocurred", 500    
    return data

@app.route('/consults/minimal')
def getConsultsSimple():
    data, err = db.getMinimalConsults()
    if  err:
        return "An unexcpeted error ocurred", 500    
    return data
