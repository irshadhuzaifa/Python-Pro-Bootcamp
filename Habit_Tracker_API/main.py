import requests
import datetime

USERNAME = "irshad-huzaifa1"
TOKEN = "abcd12345!"
GRAPH_ID = "graph1205"

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {

    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Jogging Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",

}

header = {
    "X-USER-TOKEN": TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
print(graph_response.text)

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()
print(today)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers you ran today? ")
}

pixel_create_response = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=header)
print(pixel_create_response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

update_response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
print(update_response.text)

delete_response = requests.delete(url=update_endpoint, headers=header)
print(delete_response.text)



