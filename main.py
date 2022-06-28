import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    is_prod = os.environ.get('IS_HEROKU', None)
    return 'Welcome adessi - ' + is_prod

if (__name__ == '__main__'):
    app.run(debug=True)