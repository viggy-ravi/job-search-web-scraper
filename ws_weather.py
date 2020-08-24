'''
ws_weather.py
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get request
weather = requests.get("https://forecast.weather.gov/MapClick.php?lat=30.2676&lon=-97.743#.Xjzf3WhKhPY")
print(weather.status_code)

# HTML tags relevant to forecasted weather: seven-day-forecast & forecast-tombstone
soup = BeautifulSoup(weather.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="forecast-tombstone")

# TEST CODE TO UNDERSTAND HTML STRUCTURE
# tonight = forecast_items[0]
# print(tonight.prettify())
# period = tonight.find(class_="period-name").get_text()
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
# print(temp)
# 
# img = tonight.find("img")
# desc = img['title']
# print(desc)

# Find all info
periods = [pt.get_text() for pt in seven_day.select(".forecast-tombstone .period-name")]
short_desc = [sd.get_text() for sd in seven_day.select(".forecast-tombstone .short-desc")]
temp = [t.get_text() for t in seven_day.select(".forecast-tombstone .temp")]
desc = [d['title'] for d in seven_day.select(".forecast-tombstone img")]

# Create dataframe
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_desc,
    "temp": temp,
    "desc": desc
    }
)

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night

print(weather)

