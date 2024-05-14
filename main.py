from fastapi import FastAPI, HTTPException, Query
import requests
from unidecode import unidecode
import json

app = FastAPI()

def call_api(city: str, api_key: str):
    try:
        city = unidecode(city)
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/weather/")
async def get_weather(city: str = Query(...), api_key: str = "e19e78b40afb3f90ff01b81d342fd1a5"):
    try:
        data = call_api(city, api_key)
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        
        return {
            "city": city,
            "temperature": temp,
            "pressure": pressure,
            "humidity": humidity,
            "wind_speed": wind,
            "description": description
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
