import requests
import base64
import json
import access
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def check_status(token):

    url = 'https://api.spotify.com/api/token'

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    r = requests.post(url, headers=headers).json()
    return not (r['error'] and r['error']['status'] == 401 and r['error']['message'] == 'The access token expired')

def refresh_token(ref):

    auth_client = CLIENT_ID + ':' + CLIENT_SECRET

    url = 'https://accounts.spotify.com/api/token'

    auth_encode = 'Basic ' + base64.b64encode(auth_client.encode()).decode()

    headers = {
        'Authorization': auth_encode,
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': ref
    }
    r = requests.post(url, data=data, headers=headers)
    res = r.json()
    with open('token.json', 'w') as f:
        json.dump({'token': res['access_token'],
                  'refresh': ref}, f)
    return res['access_token']
