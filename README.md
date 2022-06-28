
# Requirements
- pip install flask
- pip install pymongo
- pip install python-dotenv
- pip install pymongo[srv]


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