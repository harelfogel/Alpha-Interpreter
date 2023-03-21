from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url, ssl=True, tlsAllowInvalidCertificates=True)
db = client["smart_byte_db"]
collection = db["functions"]
