from flask import Flask
from .config import DevConfig

#Initializin application
app = Flask(__name__)

#Settin up configuration
app.config.from_object(DevConfig)

from app import views
