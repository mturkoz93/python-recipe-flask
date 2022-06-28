from flask import Flask
from data.config import CONFIG

app = Flask(__name__)

@app.route('/')
def homepage():
    try:
        return 'Welcome adessi - ' + CONFIG.is_prod + CONFIG.flask_env
    except:
        return 'There is an erro1'

if (__name__ == '__main__'):
    app.run(debug=True)