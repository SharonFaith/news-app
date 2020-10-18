from flask import Flask
#from .config import DevConfig
from config import config_options
from flask_bootstrap import Bootstrap

#initializing app 

#app = Flask(__name__, instance_relative_config = True)

#setting up configuration
#app.config.from_object(DevConfig)
#app.config.from_pyfile('config.py')

#initializing flask extensions
bootstrap = Bootstrap()

##from app import views
#from app import error

def create_app(config_name):
    app = Flask(__name__)

    #setting up configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

 #   from .request import configure_request
  #  configure_request(app)

    return app
