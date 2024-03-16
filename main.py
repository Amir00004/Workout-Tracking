import requests
from datetime import date, datetime

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
    "query": input("please enter what u did today")
}

response = requests.post(url=endpoint,json=json, headers=headers)
workout_text = response.text
workout_split = workout_text.split(',')

exercise = workout_split[9].split(':')[1]
duration = workout_split[2].split(':')[1]
calories = workout_split[4].split(':')[1]

json = {
    "workout" : {
        "date" : d1,
        "time" : current_time,
        "exercise" : exercise,
        "duration" : duration,
        "calories" : calories
    }
}

response = requests.post("YOUR_SHEETY_URL", json=json)
