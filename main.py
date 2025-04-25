import requests
import PySide6
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


latitude = 51.25
longitude = 22.57

start_date = datetime.now().date()
end_date = start_date + timedelta(days=7)

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&daily=sunrise,sunset"
    f"&hourly=temperature_2m,apparent_temperature,precipitation"
    f"&start_date={start_date}&end_date={end_date}"
    f"&timezone=Europe/Warsaw"
)

response = requests.get(url)
data = response.json()

format = "%Y-%m-%dT%H:%M"
temperature_2m = data["hourly"]["temperature_2m"]
apparent_temperature = data['hourly']['apparent_temperature']
print(temperature_2m)
x = [datetime.strptime(i, format) for i in data["hourly"]["time"]]
print(x)
plt.figure(figsize=(6,4))
plt.plot(x, temperature_2m, label='Temperatura', color='red')
plt.plot(x, apparent_temperature, label='Temperatura odczuwalna')
plt.legend()
plt.ylabel('temperatura')
plt.xlabel("czas")
plt.xticks(rotation = 45)
plt.title('Wykres')
plt.grid(True)
plt.show()

#print(data["daily"])
print(data["hourly"])