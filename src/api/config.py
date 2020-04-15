# Config params
import os

#for Google API
gspread_url = 'https://docs.google.com/spreadsheets/d/1itaohdPiAeniCXNlntNztZ_oRvjh0HsGuJXUJWET008/edit?usp=sharing'
credentials_google = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

#for Github v3 API
credentials_github = os.environ.get("GITHUB_ACCESS_TOKEN")

def twitter_api():
    consumer_key = "ejD3rnJzJPrk4pomI6Jj7xP7g"
    consumer_secret = "F8ylc7Eogk1IX4NMV47xI21fJ7gh8U8Kg5AGfIvmCizwg6YkjC"
    access_token = "69460295-I8ujKvCbwrluNsmIha7uPypSFm5dEaHm9BLIlOJnn"
    access_secret = "KgER7Ci98IR9cVej86N9BRqd6hfkPgx3ywHDqn7ndvfeA"
    return consumer_key, consumer_secret, access_token, access_secret

def aws_api():
    region = 'us-west-1'
    access_key_id = 'AKIATLC3GIPSQ4QVCZ5E'
    access_secret = '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'
    return region, access_key_id, access_secret