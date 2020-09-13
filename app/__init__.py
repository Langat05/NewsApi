from flask import Flask
from flask_bootstrap import Bootstrap
from config import *


# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object('DevConfig')
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)


    return app