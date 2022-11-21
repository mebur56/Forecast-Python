from bson import json_util
import json
import db.db as db

def save_DB(response):
    err = db.createConsult(response.json())
    return err

def save_DB_minimal(response):
    cityName = response.json()['city']['name']
    results = response.json()['list']
    consults = []
    for result in results:
        consults.append({
            "city": cityName,
            "temp_max": result["main"]["temp_max"],
            "temp_min": result["main"]["temp_min"],
            "temp": result["main"]["temp"],
            "weather": result["weather"][0]["main"],
            "datetime": result["dt_txt"]
        })
    err = db.createConsultMinimal(consults)
    response = json.loads(json_util.dumps(consults))
    return response, err