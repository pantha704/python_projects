from twilio.rest import Client
import requests, os


account_sid = "AC96949468a91c90bdf054e1c4f57f24c5"
auth_token = "bc890901bd1916565c8c65740b1e529a"

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_param = {
    "lat": 22.6161,
    "lon": 88.4363,
    "appid": "d2a0c7446760230b165fa34f30ec4211",
}
response = requests.get(OWM_Endpoint, params=weather_param)
response.raise_for_status()
print(response.json())

# to send sms alerts

client = Client(account_sid, auth_token)

message = client.messages \
    .create(body="It might rain today, Don't forget to take an umbrella.", from_="+14847491772", to="+918582995868")
