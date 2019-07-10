# used to search and collect music from spotify
import spotipy as spotify
import os
import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# username: bradysmurphy21


username = sys.argv[1]


# erasse cachhe and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

music = spotify.Spotify(auth=token) # create connection to spotify
artist = input("Enter artists name: ")

results = music.search(q=artist, limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(" ", i, t['name'])