import access
import status
import requests
import json


# with open("token.json", 'w+') as tok:
# tok.write(json.dumps(res))
# pass

song_id = '7BDQqjYCBiqtEuDzWtUaln'
song_uri = 'spotify:album:0nYshratet7NLvDRZ78yTs'

def get_album(token, id):
    # Get the album of the track to use to set the track to play
    
    url = f'https://api.spotify.com/v1/tracks/{id}'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }


    r = requests.get(url, headers=headers)
    res = r.json()
    print(res['album']['uri'])
    return res['album']['uri']

def change_song(token, uri):

    url = 'https://api.spotify.com/v1/me/player/play'

    headers = {
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/json"
    }
    data = {
        'context_uri': uri,
        'position_ms': 0
    }
    r = requests.put(url, data=json.dumps(data), headers=headers)

def print_track(token):
    url = 'https://api.spotify.com/v1/me/player/currently-playing'
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    res = requests.get(url, headers=headers)    
    r = res.json()
    temp = 'Currently Playing:'

    print(r['item']['uri'])
    
    print(' '.join([temp, r['item']['name'],'by', r['item']['artists'][0]['name']]))


with open("token.json", 'r+') as f:
    if len(f.read()) == 0:
        res = access.access()
        json.dump({'token': res['access_token'],
                  'refresh': res['refresh_token']}, f)
    else:
        f.seek(0)
        temp = json.loads(f.read())
        token = temp['token']
        refresh = temp['refresh']

        if status.check_status(token):
            print("Works")
            print_track(token)
            # uri = get_album(token, song_id)
            # change_song(token, uri)
        else:
            print("refreshed")
            token = status.refresh_token(refresh) 
