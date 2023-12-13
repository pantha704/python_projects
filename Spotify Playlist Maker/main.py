import os

import requests, spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

CLIENT_ID = "53e11990fce2489891c408780701d62b"
CLIENT_SECRET = "dfb91849a3ad4b12956874bafcc0a50b"

time = input("Which year would you like to travel to? Type the date in YYYY-MM-DD format: ")

response = requests.get(url="https://www.billboard.com/charts/hot-100/2000-08-12/")
data = response.text
soup = BeautifulSoup(data, 'html.parser')
music_data = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
music_list = [music.getText().strip() for music in music_data]
print(music_list)

# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com/",
#         client_id=os.environ["SPOTIPY_CLIENT_ID"],
#         client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
#         show_dialog=True,
#         cache_path="token.txt",
#     )
# )
# user_id = sp.current_user()["id"]
