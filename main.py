import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

account_sid = "AC6dba88d0d3b9d5bf31f48a6890774dd8"
auth_token = "94a371903aaac2e0cc4511991c06b45b"
api_key = "65c55144e13af6cbfc706faea279a484"

# To check the code, hash below two lines. Also remove http_client=proxy_client on line 38.
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
         from_='+19896608055',
         to='+917550168737'
         )
    print(message.status)
#THE END :)
