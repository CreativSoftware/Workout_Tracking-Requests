import requests
from datetime import datetime


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GENDER = "male"
WEIGHT_KG = 95.25
HEIGHT_CM = 15.24
AGE = 40

USERNAME = ""
PASSWORD = ""

APP_ID = ""
API_KEY = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/4f8ef46e6ac6156262f9804f34d24cff/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD))

    print(sheety_response.text)
