
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
