from pymongo import MongoClient
from dotenv import load_dotenv
import os
import re

class Controller:
    def __init__(self):
        load_dotenv()
        mongo_url = os.getenv('MONGO_URL')
        client = MongoClient(mongo_url, ssl=True, tlsAllowInvalidCertificates=True)
        self.db = client["smart_byte_db"]
        self.collection = self.db["functions"]

    def get_collection(self):
        return self.collection

    def get_vars(self):
        vars_collection = self.db["sensor_values"]
        vars = vars_collection.find()
        with open("example.txt", 'w') as file:
            for var in vars:
                file.write(var.get('value') + "\n")
            file.close()

    def get_functions(self):
        function_collection = self.db["rules"]
        rules = function_collection.find()
        with open("example.txt", 'a') as file:
            for rule in rules:
                if self.check_if_need_to_write_action(rule.get('rule')):
                    file.write(rule.get('rule') + "\n")
            file.close()

    def check_if_need_to_write_action(self, rule):
        device_name = self.get_device_from_rule_string(rule).lower()
        desired_state = self.get_state_from_rule_string(rule).lower()
        device = self.db["devices"].find_one({"name": device_name})
        if desired_state != device.get('state'):
            return True
        return False

    def get_device_from_rule_string(self, rule):
        start_index = rule.find('PRINT("') + len('PRINT("')
        end_index = rule.find('")', start_index)
        substring = rule[start_index:end_index]
        return substring.split()[-1]

    def get_state_from_rule_string(self, rule):
        pattern = r"off|on"
        match = re.search(pattern, rule)
        if match:
            result = match.group(0)
            return result
