import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MY_LAT = 42.829939
MY_LNG = 74.583855

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("MY_KEY")
account_sid = "MY_SID"
auth_token = os.environ.get("MY_AUTH_TOKEN")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="435645333",
        to="3456554366"
    )
    print(message.status)
