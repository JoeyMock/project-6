"""
Brevets RESTful API
"""
import os
from flask import Flask
from flask_restful import Api
from mongoengine import connect
# You need to implement two resources: Brevet and Brevets.
# Uncomment when done:
from resources.brevet import Brevet
from resources.brevets import Brevets

# Connect MongoEngine to mongodb
connect(host=f"mongodb://{os.environ['MONGODB_HOSTNAME']}:27017/brevetsdb")

# Start Flask app and Api here:
app = Flask(__name__)
api = Api(app) 
#start soon

# Bind resources to paths here:
api.add_resource(Brevet, "/api/brevet/<id>")
api.add_resource(Brevets, "api/brevets") 

if __name__ == "__main__":
    # Run flask app normally
    # Read DEBUG and PORT from environment variables.
    print({os.environ["PORT"]})
    app.run(port=os.environ["PORT"], host = "0.0.0.0")
    
