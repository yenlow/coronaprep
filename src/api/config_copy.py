# Config params
# Fill in with your credentials and rename file to config.py

import os

#for Google API
gspread_url = 'http://xxx'
credentials_google = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") #assuming you save keys as env variables

#for Github v3 API
credentials_github = os.environ.get("GITHUB_ACCESS_TOKEN") #assuming you save keys as env variables

def twitter_api():
    consumer_key = "xxx"
    consumer_secret = "xxx"
    access_token = "xxx"
    access_secret = "xxx"
    return consumer_key, consumer_secret, access_token, access_secret

def aws_api():
    region = 'us-west-1'
    access_key_id = 'xxx'
    access_secret = 'xxx'
    return region, access_key_id, access_secret