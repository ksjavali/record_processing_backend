from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB URI from environment variables
uri = os.getenv("MONGODB_URI")

# Create a new MongoClient instance and connect to the MongoDB server
client = MongoClient(uri, server_api=ServerApi('1'))

# Select the database and collection
db = client.todo_db
collection = db["records"]
