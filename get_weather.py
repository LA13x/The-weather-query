import json
from os import chdir
import pickle
import requests


def getCityTemp(cityName):
    with open("../city.pkl", 'rb') as cityInfo:
        city = pickle.load(cityInfo)

    cityNumber = city[cityName]

    url = "http://www.weather.com.cn/data/cityinfo/" + cityNumber + ".html"

    html = requests.get(url)
    html.encoding = "utf-8"
    jsonData = json.loads(html.text)
    # print(jsonData)

    city = jsonData["weatherinfo"]["city"]
    minTemp = jsonData["weatherinfo"]["temp1"]
    maxTemp = jsonData["weatherinfo"]["temp2"]
    weather = jsonData["weatherinfo"]["weather"]
    ptime = jsonData["weatherinfo"]["ptime"]

    return city, minTemp, maxTemp, weather, ptime
