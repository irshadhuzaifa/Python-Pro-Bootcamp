import json
import requests
import datetime
import os

APP_ID = os.environ.get("ENV_APP_ID")
TOKEN = os.environ.get("ENV_TOKEN")
API_KEY = os.environ.get("ENV_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": input("How much exercise you did today? "),
    "weight_kg": 54,
    "height_cm": 163,
    "age": 25,
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=header)
exercise_data = exercise_response.text
# print(type(exercise_data))
all_data = json.loads(exercise_data)
# print(all_data)

exercise_name = all_data["exercises"][0]["name"]
# print(exercise_name)
exercise_time = all_data["exercises"][0]["duration_min"]
# print(exercise_time)
exercise_calories = all_data["exercises"][0]["nf_calories"]
# print(exercise_calories)

sheety_enpoint = os.environ.get("ENV_SHEETY_ENDPOINT")

sheety_header = {
    "Authorization": TOKEN
}
spreadsheet_data = requests.get(url=sheety_enpoint, headers=sheety_header)
#print(spreadsheet_data.text)

curr_date = datetime.datetime.now().strftime("%d/%m/%Y")
curr_time = datetime.datetime.now().strftime("%H:%M:%S")
# print(curr_date)
# print(curr_time)


row_data = {
    "workout":
        {
            "date": curr_date,
            "time": curr_time,
            "exercise": exercise_name.title(),
            "duration": exercise_time,
            "calories": exercise_calories,
        }
}

response = requests.post(url=sheety_enpoint, json=row_data, headers=sheety_header)
print(response.text)