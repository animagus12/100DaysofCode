from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import creds


URL = "https://www.billboard.com/charts/hot-100/"
TITLES_CLASS = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
FIRST_CLASS = "c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-r-150"
CLIENT_ID = creds.CLIENT_ID
CLIENT_SECRET = creds.CLIENT_SECRET
REDIRECT_URI = "http://example.com"


# -----------------------------------------------Scraping Billboard 100-----------------------------------------------
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = (requests.get(f"{URL}{date}/")).text
soup = BeautifulSoup(response, "html.parser")

titles = soup.find_all(
    name="h3",
    class_=TITLES_CLASS,
    id="title-of-a-story")

number_one = soup.find(name="h3", class_=FIRST_CLASS, id="").text
number_one = number_one.replace("\n", "")

top_titles = []

top_titles.append(number_one)

for title in titles:
    top_titles.append((title.getText()).replace("\n", ""))

# print(top_titles)
# ------------------------------------------------------------------------------------------------------------------------



# -------------------------------------------------Spotify Authentication-------------------------------------------------
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="Day 46/token.txt"
    )
)
user_id = sp.current_user()["id"]
# ------------------------------------------------------------------------------------------------------------------------



# ------------------------------------------Searching Spotify for songs by title------------------------------------------
song_uris = []
year = date.split("-")[0]
for title in top_titles:
    result = sp.search(q=f"track:{title} year:{year}", type='track', market=None)
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")
    
# print(song_uris)
# ------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------Creating a new private playlist---------------------------------------------
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
# ------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------Adding songs into the playlist---------------------------------------------
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
# ------------------------------------------------------------------------------------------------------------------------