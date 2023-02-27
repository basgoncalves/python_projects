# import pyforest as py
from .utils.imports import *

client_credentials_manager = SpotifyClientCredentials(client_id='basgoncalves', client_secret='picklerick_FB7')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# https://blog.devgenius.io/spotify-data-analysis-with-python-a727542beaa7