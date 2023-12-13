import smtplib

import requests, datetime, time

MY_LAT = 22.6161
MY_LONG = 88.4360
MY_EMAIL = "prathamjaiswal204@gmail.com"
PASSWORD = "rhhxzirrnqoisxbi"


def is_night():
    parameter = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data['results']['sunrise'].split('T')[1].split('+')[0].split(":")[0])
    sunset = int(data['results']['sunset'].split('T')[1].split('+')[0].split(":")[0])
    now = datetime.datetime.now()
    if now.hour >= sunset or now.hour <= sunrise:
        return True


def iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    # print(response.raise_for_status())
    # print()
    # print(response.json())
    # print()
    # print(response.status_code)

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    # print(data)
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True


while True:
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: Look Up!\n\nThe"
                                                                           " ISS is above you in the sky.")
            connection.close()
    time.sleep(60)
