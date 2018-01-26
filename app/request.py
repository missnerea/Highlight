from app import app
from urllib.request,json
from .models import article

#Getting api key
api_key = app.config['NEWS_API_KEY']
