import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class Database:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]


db = Database(
    "mongodb+srv://dhairya:"
    + os.environ.get("mongoPW")
    + "@cluster0.vpuxf.mongodb.net/?retryWrites=true&w=majority",
    db_name="test",
)
