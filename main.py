import requests
from fastapi import FastAPI

app = FastAPI()

# Khai báo API key của OpenWeatherMap
API_KEY = "e06657dd707b4bd0e3ad3b032ceb9a33"

@app.get("/")
async def read_data():
    # Gửi yêu cầu GET đến API của OpenWeatherMap
    city = "Bac Giang"  # Thành phố bạn muốn lấy dữ liệu
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Lấy dữ liệu từ phản hồi JSON
        data = response.json()
        # Trích xuất nhiệt độ và độ ẩm từ dữ liệu
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        # Trả về dữ liệu
        return {"temperature": temperature, "humidity": humidity}
    else:
        # Trả về lỗi nếu không thể lấy dữ liệu
        return {"error": "Failed to fetch data from OpenWeatherMap API"}
