import requests, datetime as dt
import json

APP_ID = "ac5755a6"
API_KEY = "9a7b194fb9ae0e9b945606b54fa0b67d"
ID = "8d47e689-9e2e-43ad-b604-75938d8a3c1b"

URL = "https://trackapi.nutritionix.com/v2"
BEARER = "sdwdsadwgrhgdmapmfsdmgernginfvnvafaopfdsaew"

SIGN_UP_PARAM = {
    "password": "prathamj!",
    "email": "pratham.jaiswal2004@gmail.com",
    "first_name": "Pratham",
    "timezone": "UTC",
    "ref": "string"
}

response = requests.post(url=f"{URL}/auth/signup", json=SIGN_UP_PARAM, headers={})
print(response.status_code)

SIGN_IN_PARAM = {
    "password": "prathamj!",
    "email": "pratham.jaiswal2004@gmail.com",
}
response = requests.post(url=f"{URL}/auth/signin", json=SIGN_IN_PARAM)
print(response.status_code)

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
HEADERS2 = {
    # "x-app-id": APP_ID,
    # "x-app-key": API_KEY,
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json",
}
qry = input("Throw your story: ")
print(qry)
EXERCISE_PARAM = {
    "query": qry,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 177.0,
    "age": 19,
}

response = requests.post(url=f"{URL}/natural/exercise", params=EXERCISE_PARAM, data=EXERCISE_PARAM, json=EXERCISE_PARAM
                         , headers=HEADERS)
# response.raise_for_status()
result = response.json()
print(result)

today = dt.datetime.now().strftime("%d/%m/%Y")
now = dt.datetime.now().strftime("%X")

USERNAME = "de02017935ae516e43c746f6aebbd6a0"
PROJECT_NAME = "workoutTracking"
SHEET_NAME = "sheet1"
SHEETY_URL = "https://api.sheety.co"
SHEETY_PARAM = {}

for exercise in result['exercises']:
    SHEETY_PARAM = {
        "sheet1": {
                "date": today,
                "time": now,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
        }
    }


response2 = requests.post(url=f"{SHEETY_URL}/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}", json=SHEETY_PARAM, headers=HEADERS2)
print(response2.text)
