import json
import os
from dotenv import load_dotenv

load_dotenv()
db_path = os.getenv("DB_PATH")

def load_db():
    with open(db_path,'r') as file_data:
        data=json.load(file_data)
    return data

def save_db(data):
    with open(db_path,'w')as file_data:
        json.dump(data,file_data,indent=4)