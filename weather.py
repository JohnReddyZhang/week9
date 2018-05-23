# This is the weather module.
import keys
from urllib.request import urlopen
from twilio.rest import Client
import json


def is_valid(number, digits):
    if len(number) != digits or not number.isdigit():
        return False


def get_degree(zip_code):
    if not is_valid(zip_code, 5):
        return False
    url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zip_code \
          + ",us&units=imperial&appid=" + keys.weather_api
    raw_json = urlopen(url).read()
    data = json.loads(raw_json)
    temp = data['main']['temp']
    return str(round(temp))


def send_text(phone_number):
    if not is_valid(phone_number, 10):
        return False



    client = Client(keys.account_sid, keys.auth_token)

    sms_body = "It is " + str(round(temp)) + " degrees outside."
    message = client.messages.create(
        body=sms_body,
        from_=keys.from_number,
        to='+1' + phone
    )
