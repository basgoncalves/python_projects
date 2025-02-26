import pandas as pd
import os
class utils:
    def __init__(self):
        pass

    def get_spotify_data(self):
        pass


# https://blog.devgenius.io/spotify-data-analysis-with-python-a727542beaa7

url = r'https://kworb.net/spotify/country/global_daily.html'
df = pd.read_html(url)[0]
print(df.head(5))

import pdb; pdb.set_trace()