#contains database and application instances.
from flask import Flask
#from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config



db = SQLAlchemy()  #DB instance is defined
# note: Job class is sub class of db.Model class
#bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    
 #   Bootstrap(app)
    db.init_app(app)    
    return app

#The create_app() function is used to create the app 
# instance based on the environment, which is passed as an argument to the function through the config_name parameter.
#The app.config.from_object() method is used to load the configuration from the config dictionary. Then that config is 
#used to initialize the app. Finally, 
#the SQLAlchemy instance db is initialized with the app instance.