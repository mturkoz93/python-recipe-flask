# About App
I developed a backend service about adding recipes and listing.

The git repo is connected to <b>Heroku</b> and when the master branch is triggered, automatic deploy starts.

It uses <b>mongodb</b> on mongoatlas as a database service.


### Methods
<b>base_url:</b> https://adesso-recipe-flask.herokuapp.com/

<b>list all recipes (GET):</b> https://adesso-recipe-flask.herokuapp.com/recipes

<b>get a single recipe (GET):</b> https://adesso-recipe-flask.herokuapp.com/recipes/:recipe_id

<b>create a new recipe (POST):</b> https://adesso-recipe-flask.herokuapp.com/recipes


# Requirements
- pip install flask
- pip install pymongo
- pip install python-dotenv
- pip install pymongo[srv]

# Add .env file
```
export FLASK_APP=app
export FLASK_ENV=development
export TEST=test
export IS_HEROKU=test

export DB_USERNAME=
export DB_PASSWORD=
```

# Heroku - Create a new Git repository
- cd my-project/
- git init
- heroku git:remote -a adesso-recipe-flask

# Heroku - Deploy your application
- git add .
- git commit -am "make it better"
- git push heroku master

# Heroku - Existing Git repository
heroku git:remote -a adesso-recipe-flask

# Heroku - Deployment
- https://www.heroku.com/python
