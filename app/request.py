from app import app
from urllib.request,json
from .models import Articles, Sources

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting article base url
base_url= app.config['NEWS_API_BASE_URL']
