from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url, ssl=True, tlsAllowInvalidCertificates=True)
db = client["smart_byte_db"]
collection = db["functions"]


def getVars():
    varsCollection = db["sensor_values"]
    cursor = varsCollection.find()
    with open("example.txt", 'w') as file:
        for document in cursor:
            file.write(document.get('value') + "\n")
        file.close()
def getFunctions():
    functionCollection = db["rules"]
    cursor = functionCollection.find()
    with open("example.txt", 'a') as file:
        for document in cursor:
            file.write(document.get('rule') + "\n")
        file.close()
    client.close()
