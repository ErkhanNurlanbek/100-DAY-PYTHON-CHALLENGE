import pip
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup


user_inp = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = user_inp.split('-')[0]
CLIENT_ID = 'ba7e9317a49444c08ac7a59608ae81fb'
CLIENT_SECRET = 'abb7ccb4b4cd453cad227d66f41be2ca'
ACCESS_TOKEN = {"access_token": "BQBc4NX0HeMV4M9C7uZTmS3wPlqQIwaGHoB-LF8_Gtq1bBSnC26wshhggFNZhVcCSrpknev45IS2lo8D1KAsnODd7UEL9wyqSpijnc3Gx1jeYZyPAcOlQuuhf7UNkTnhXk4u36vpZ-JG0tyZoLxDid--cnEpW6ZR0qxpbTOwexI8wNDzv-cfzQuZTbPj1-_k7wwdrt9JXasHR9orogvhwtyzmfICgs1efLg9LmbbC5cEPVuTB2BkC4UsgnwPYYqlNHXG3w", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQAfLkxhCWlYcH2w--oIEXKd_7XD5wIHZhKvLbGkn0EWIym65crjiIclxWTZIWQPM5eSz0C-Gq6gc94Dzu7b0IAT6IxA1D7IxBVcePvyi-wzS9pCPJsQgVQVtJ1_G7q5UqU", "scope": "playlist-modify-private", "expires_at": 1740158500}


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


response = requests.get('https://www.billboard.com/charts/hot-100/' + user_inp, headers=header)

billboard_WEB = response.text
soup = BeautifulSoup(billboard_WEB, 'html.parser')

l = soup.select('li ul li h3')
song_uris = [v.getText().strip() for v in l]

# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope= "playlist-modify-private",
#         redirect_uri='http://example.com',
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         show_dialog=True,
#         cache_path='token.txt',
#         username='313qyl22wkb3vpcyixwphyxrb7l4'
#     )
# )
# user_id = sp.current_user()['id']
#
# 'AQAYHpHeAiPAhyzH9FOb4zwzjJswmgp6wt0yeOEPNSRipf1ftZG3TH1oZkL2o3FMbEh5fmwls03nMpDoxf4cf5YVOye5sfJ0_RqZg6WsOJeh90b4AsRP1l0Awibo9rj7npkpof1aEwJ7bh1IB3YMy8cfPyRMxT72Gvc'
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp0 = spotipy.client.Spotify(auth=ACCESS_TOKEN['access_token'], requests_session=True)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='313qyl22wkb3vpcyixwphyxrb7l4',
    )
)

print(sp0.current_user()['id'])

user_id = sp.current_user()["id"]
song_names = ["The list of song", "titles from your", "web scrape"]

playlist = []
for song in song_uris:
    result = sp0.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_uri = result['tracks']['items'][0]['uri']
        playlist.append(song_uri)
    except IndexError:
        print('Song is not available.')
        continue
print(playlist)


playlistid = sp0.user_playlist_create(user=user_id, name=f'{year} Billboard 100', public=False, description='music lane')['id']

print(sp0.playlist_add_items(playlist_id=playlistid, items=playlist))











