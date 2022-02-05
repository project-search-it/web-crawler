import pymongo
import os

from dotenv import load_dotenv
load_dotenv()

mongo_client = os.getenv('mongoClient')
db_name = os.getenv('databaseName')

client = pymongo.MongoClient(mongo_client)

db = client.get_database(db_name)

# TODO: Finish mongo db implementation here