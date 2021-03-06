from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
from data.db import *

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'This is an api service for recipe.'

"""
list all recipes.
"""
@app.route('/recipes', methods = ['GET'])
def listAllRecipes():
    try:
        recipes = list(db.recipes.find())
        for recipe in recipes:
           recipe['_id'] = str(recipe['_id'])

        return Response(
            response= json.dumps(recipes),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({'message': 'cannot read recipes!'}),
            status=500,
            mimetype='application/json'
        )

"""
get a single recipe
"""
@app.route('/recipes/<string:recipe_id>', methods= ['GET'])
def getRecipe(recipe_id):
    try:
        recipe = db.recipes.find_one({ '_id': ObjectId(recipe_id) })
        recipe['_id'] = str(recipe['_id'])

        return Response(
            response= json.dumps(recipe),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({'message': 'cannot read recipe!'}),
            status=500,
            mimetype='application/json'
        )


"""
create a new recipe.
"""
@app.route('/recipes', methods = ['POST'])
def createRecipe():
    try:
        payload = request.get_json()

        new_recipe = {
            "title": payload['title'],
            "steps": payload['steps'],
        }

        dbResponse = db.recipes.insert_one(new_recipe)

        return Response(
            response= json.dumps(
                {'message': 'recipe created', 
                'recipe_id': f'{dbResponse.inserted_id}'
                }
            ),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({'message': 'cannot create recipe!'}),
            status=500,
            mimetype='application/json'
        )

"""
update the recipe.
"""
@app.route('/recipes/<string:recipe_id>', methods = ['PATCH'])
def updateRecipe(recipe_id):
    try:
        payload = request.get_json()

        myquery = { "_id": ObjectId(recipe_id) }
        newvalues = { "$set": { "title": payload['title'], "steps": payload['steps'] } }

        db.recipes.update_one(myquery, newvalues)

        return Response(
            response= json.dumps(
                {
                    'message': 'recipe updated', 
                    'success': True
                }
            ),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({'message': 'cannot update recipe!'}),
            status=500,
            mimetype='application/json'
        )
        
"""
delete the recipe.
"""
@app.route('/recipes/<string:recipe_id>', methods = ['DELETE'])
def deleteRecipe(recipe_id):
    try:

        myquery = { "_id": ObjectId(recipe_id) }

        db.recipes.delete_one(myquery)

        return Response(
            response= json.dumps(
                {
                    'message': 'recipe deleted', 
                    'success': True
                }
            ),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({'message': 'cannot delete recipe!'}),
            status=500,
            mimetype='application/json'
        )
# *************************************

if (__name__ == '__main__'):
    app.run(debug=True)
