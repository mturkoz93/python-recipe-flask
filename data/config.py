import os

class CONFIG:
    test = os.environ.get('TEST', None)
    is_prod = os.environ.get('IS_HEROKU', None)
    flask_env = os.environ.get('FLASK_ENV', None)
    db_username = os.environ.get('DB_USERNAME', None)
    db_password = os.environ.get('DB_PASSWORD', None)