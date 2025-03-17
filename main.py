import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("OWM_API_KEY")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

# coordinates
LAT = 0
LON = 0

parameters = {
    "lat": LAT,
    "lon": LON,
    "units": "metric",
    "cnt": 4,
    "appid": API_KEY
}

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=ENDPOINT, params=parameters)

response.raise_for_status()
data = response.json()

condition_list = [data["weather"][0]["id"] for data in data["list"]]

will_rain = False
for condition in condition_list:
    if condition < 700:
        will_rain = True
        break

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="Vai chover hoje. Leve um guarda-chuva! ☔",
        from_="+13344661705",
        to="+0000000000",
    )
    print(message.body)


