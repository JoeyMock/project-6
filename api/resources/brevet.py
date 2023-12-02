"""
Resource: Brevet
"""
from flask import Response, request
from flask_restful import Resource
from mongoengine.errors import DoesNotExist

# You need to implement this in database/models.py
from database.models import Brevet

# MongoEngine queries:
# Brevet.objects() : similar to find_all. Returns a MongoEngine query
# Brevet(...).save() : creates new brevet
# Brevet.objects.get(id=...) : similar to find_one

# Two options when returning responses:
#
# return Response(json_object, mimetype="application/json", status=200)
# return python_dict, 200
#
# Why would you need both?
# Flask-RESTful's default behavior:
# Return python dictionary and status code,
# it will serialize the dictionary as a JSON.
#
# MongoEngine's objects() has a .to_json() but not a .to_dict(),
# So when you're returning a brevet / brevets, you need to convert
# it from a MongoEngine query object to a JSON and send back the JSON
# directly instead of letting Flask-RESTful attempt to convert it to a
# JSON for you.

class Brevet(Resource):
    def get(self, brevet_id):
        try:
            return Response(
                    Brevet.objects.get(id=brevet_id).to_json(), 
                    mimetype = "application/json", 
                    status = 200
            )
        except DoesNotExist:
            return {"error: doesn't exist"}, 404
        except Exception as ex:
            return {"error": str(ex)}, 500

    def put(self, brevet_id):
        try:
            Brevet(**request.json).validate()   #is it valid?
            new_docs = Brevet.objects.get(id=brevet_id).update(
                    __raw__ = {"$set": request.json}
            )
            if docs_updated == 1:
                return {"put in"}, 200
            else:
                return {"error: internal"}, 500
        except DoesNotExist:
            return {"error: no brevet for this id found"}, 404
        except Exception as ex:
            return {"error": str(ex)}, 500

    def delete(self, brevet_id):
        try:
            Brevet.objects.get(id = brevet_id).delete()
            return {"success"}, 500
        except Exception as ex:
            return {"error": str(ex)}, 500
