import os

class CONFIG:
    test = os.environ.get('TEST', None)
    is_prod = os.environ.get('IS_HEROKU', None)
    flask_env = os.environ.get('FLASK_ENV', None)