import unittest
import weather
import keys
from sys import exit
from urllib.request import urlopen
from twilio.rest import Client
import json


def degrees():
    url = "http://api.openweathermap.org/data/2.5/weather?zip=" + '60637' + \
          ",us&units=imperial&appid=" + keys.weather_api
    raw_json = urlopen(url).read()
    data = json.loads(raw_json)
    temp = data['main']['temp']
    return str(round(temp))


class Test0(unittest.TestCase):
    def test0d(self):
        print(degrees())

    def test0get_weather(self):
        w = weather.get_degree('60637')
        self.assertEqual(w, degrees())


if __name__ == '__main__':
    unittest.main()