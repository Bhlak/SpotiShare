import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

redirect_uri = "https://localhost:3000"

authorization_base_url = "https://accounts.spotify.com/authorize"
AUTH_URL = 'https://accounts.spotify.com/api/token' 

scope = [
    'user-read-playback-state',
    'user-modify-playback-state',
    'user-read-currently-playing',
    'user-read-playback-position'
]

sesh = OAuth2Session(CLIENT_ID, scope=scope, redirect_uri=redirect_uri)

authorization_url, state = sesh.authorization_url(authorization_base_url)


def access():
    print("Authorize:", authorization_url)

    res = input("\nInput redirect uri: ")

    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    token = sesh.fetch_token(AUTH_URL, auth=auth, authorization_response=res)

    return token
