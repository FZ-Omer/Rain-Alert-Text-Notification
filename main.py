import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
import os


load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
api_key = os.getenv("api_key")
twilio_number = os.getenv("twilio_number")
my_number = os.getenv("my_number")

# To check the code, hash below two lines. Also remove http_client=proxy_client on line 67.
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

parameters = {
    "lat": 13.082680,
    "lon": 80.270721,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# print(response.status_code)
response.raise_for_status()
data = response.json()
id_list = []
for data in data["hourly"][:13]:
    id_list.append(data["weather"][0]["id"])

# print(id_list)

will_rain = False
for each_id in id_list:
    if each_id < 700:
        will_rain = True

if will_rain:
    # print("Bring the Umbrella!!")
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
         body="HELLO FZ! It's seems gonna Rain Today. Don't forget to plan your travel accordingly!! ☔ ",
         from_=twilio_number,
         to=my_number
         )
    print(message.status)
