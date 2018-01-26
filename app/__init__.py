from flask import Flask

#Initializin application
app = Flask(__name__)

from app import views
