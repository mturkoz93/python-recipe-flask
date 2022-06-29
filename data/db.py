import pymongo

from dotenv import load_dotenv
load_dotenv()

from data.config import CONFIG

"""
mongo connection
"""
try:
    CONNECTION_STRING = 'mongodb://localhost:27017/recipe' if CONFIG.flask_env == 'development' else f'mongodb+srv://{CONFIG.db_username}:{CONFIG.db_password}@cluster0.izwr5.mongodb.net/recipe?retryWrites=true&w=majority'
    mongo = pymongo.MongoClient(CONNECTION_STRING)
    db = mongo.recipe # database name
    mongo.server_info() # trigger exception if cannot connect to db
except Exception as ex:
    print(ex)
    print('ERROR - Cannot connect to db')
# *************************************