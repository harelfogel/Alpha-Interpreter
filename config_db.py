from pymongo import MongoClient
from dotenv import load_dotenv
import os
import re

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url, ssl=True, tlsAllowInvalidCertificates=True)
db = client["smart_byte_db"]
collection = db["functions"]


def get_vars():
    vars_collection = db["sensor_values"]
    vars = vars_collection.find()
    with open("example.txt", 'w') as file:
        for var in vars:
            file.write(var.get('value') + "\n")
        file.close()
def get_functions():
    function_collection = db["rules"]
    rules = function_collection.find()
    with open("example.txt", 'a') as file:
        for rule in rules:
            if check_if_need_to_write_action(rule.get('rule')):
                file.write(rule.get('rule') + "\n")
        file.close()


def check_if_need_to_write_action(rule):
    device_name = get_device_from_rule_string(rule).lower()
    desired_state = get_state_from_rule_string(rule)
    device = db["devices"].find_one({"name": device_name})
    if desired_state != device.get('state'):
        return True
    return False

def get_device_from_rule_string(rule):
    start_index = rule.find('PRINT("') + len('PRINT("')
    end_index = rule.find('")', start_index)
    substring = rule[start_index:end_index]
    return substring.split()[-1]

def get_state_from_rule_string(rule):
    pattern = r"off|on"
    match = re.search(pattern, rule)
    if match:
        result = match.group(0)
        return result

get_vars()
get_functions()
# IF temperature>10 AND ac==off THEN PRINT(turn on Ac)