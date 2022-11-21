from pymongo import MongoClient
from dotenv import load_dotenv
from bson import json_util
import json
import os

load_dotenv()

client = MongoClient()
CONNECTION_STRING = os.getenv('CONNECTION_STRING')
client = MongoClient(CONNECTION_STRING)
db = client['forecast']
collection_minimal = db['minimal_consults']
collection = db['consults']



def createConsult(consults):
    try:
        collection.insert_one(consults)
        return
    except Exception as err:
        return err

def getConsults():
    try:
     cursor = collection.find({})
     list_cur = list(cursor)
     response = json.loads(json_util.dumps(list_cur))
     return response, None
    except Exception as err:
        return None, err

def createMinimalConsult(consults):
    try:
        collection_minimal.insert_many(consults)
        return None
    except Exception as err:
        return err

def getMinimalConsults():
    try:
     cursor = collection_minimal.find({})
     list_cur = list(cursor)
     response = json.loads(json_util.dumps(list_cur))
     return response, None
    except Exception as err:
        return None, err

    
