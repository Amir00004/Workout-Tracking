import requests
from datetime import date, datetime

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 174
AGE = 20

today = date.today()
d1 = today.strftime("%d/%m/%Y")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

APP_ID = "YOUR_API_ID"
APP_KEY = "YOUR_API_KEY"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

json = {
    "query": input("please enter what u did today"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=endpoint,json=json, headers=headers)
workout_text = response.json()

for exercise in workout_text["exercises"]:
    json = {
        "workout": {
            "date": d1,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


response = requests.post("YOUR_SHEETY_URL", json=json)
