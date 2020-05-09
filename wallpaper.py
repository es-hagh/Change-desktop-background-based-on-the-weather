#make sure that all of the modules are installed
import ctypes
import datetime
import os
import time
from datetime import date

import requests


def set_wallpaper(wallpaper_path=None):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3)


def get_wallpaper_key(timestamp, current_weather):
    if date.today().weekday() == 6:
        return "Sunday"
    if current_weather == "Rain":
        return "Rain"
    elif current_weather == "Thunderstorm":
        return "Storm"
    elif current_weather == "Drizzle":
        return "Drizzle"
    elif current_weather == "Clear" and START_NIGHT <= timestamp or timestamp <= END_NIGHT:
        return 'Night'
    elif current_weather == "Clear" and START_DAY <= timestamp <= END_DAY:
        return "Day"
    elif current_weather == "Clouds":
        return "Clouds"
    else:
        return "Other"


SPI_SETDESKWALLPAPER = 20

#set addres of your wallpapers folder after 'r'
WALLPAPERS_DIR = r"C:\Users\611\Desktop\first copy project\wallpaper"

API_ADDRESS = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

#Add your city name here
CITY = "Where are you live"
WEATHER_REFRESH_RATE = 120
COMPLETE_API_URL = f'{API_ADDRESS}{CITY}'

START_NIGHT = datetime.time(18, 1)
END_NIGHT = datetime.time(6, 0)
START_DAY = datetime.time(6, 1)
END_DAY = datetime.time(18, 0)

# Set your wallpaer to options
# 'Wheather' : 'your wallpaper+file format' 
weather_wallpaper_filename_dict = {
    'Sunday': 'cepscope.jpeg',
    'Rain': 'cepscope-02.jpeg',
    'Storm': 'etts-01.png',
    'Drizzle': 'etts-02.JPG',
    'Night': 'etts-03.jpg',
    'Day': 'paksumatik.jpg',
    'Clouds': 'paksumatik-team.jpg',
    'Other': 'pulsotizm.jpg'
}

if __name__ == '__main__':
    while True:
        timestamp = datetime.datetime.now().time()
        json_data = requests.get(COMPLETE_API_URL).json()
        format_data = json_data["weather"][0]["main"]
        wallpaper_key = get_wallpaper_key(timestamp=timestamp, current_weather=format_data)
        wallpaper_path = os.path.join(WALLPAPERS_DIR, weather_wallpaper_filename_dict[wallpaper_key])
        set_wallpaper(wallpaper_path)
        time.sleep(WEATHER_REFRESH_RATE)