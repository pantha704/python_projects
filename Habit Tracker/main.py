import requests, datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
token = "sadasadasadasada4"
username = "pantha704"

user_params = {
    "token": "sadasadasadasada4",
    "username": "pantha704",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
id = "habit-graph"

graph_config = {
    "id": "habit-graph",
    "name": "Habit Tracker",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}
header = {
    "X-USER-TOKEN": token,
}

response2 = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(response2.text)

today = dt.datetime.now()

# year = today.year
# month = today.month
# day = today.day
# if month < 10:
#     month = f"0{month}"
# if day < 10:
#     day = f"0{day}"
# print(f"{year}{month}{day}")

graph_url = f"{graph_endpoint}/{id}"
pixel_param = {
    "date": today.strftime('%Y%m%d'),
    "quantity": "44",
}
response3 = requests.post(url=graph_url, json=pixel_param, headers=header)
print(response3.text)

update_endpoint = f"{graph_url}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4",
}
response4 = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
print(response4.text)

response5 = requests.delete(url=update_endpoint, headers=header)
print(response5.text)