import datetime
import random
import time
from subprocess import Popen

import requests
from faker import Faker
import os
from selenium import webdriver
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.webkitgtk.options import Options

from ClickMeetingRestClient import ClickMeetingRestClient


url = 'http://127.0.0.1:8000'

# API
# def get_settings_from_web(url):
#     settings = {
#         'api_key': requests.get(url + '/api/api_key').json()[0],
#         'general_settings': requests.get(url + '/api/general_settings').json()[0],
#         'room_id': requests.get(url + '/api/room_id').json()[0],
#         'timeline': get_timelines(url),
#     }
#     resp = requests.get(url + '/api/bots').json()
#     bots = []
#     for bot in resp:
#         if bot['geo'] == settings['general_settings']['geo']:
#             bots.append(bot)
#     settings['bots'] = bots
#     return settings


# settings = get_settings_from_web(url)
# for item in settings.items():
#     print(item)



# def get_timelines(url):
#     response = requests.get(url + '/api/timeline').json()
#     result = {}
#     for item in response:
#         key = item['name']
#         value = item['commands']
#         result[key] = value
#     return result
#
#
# l = get_settings_from_web(url)

# SORTED TIME
# l = []
# for i in range(10):
#     now = datetime.datetime.now().time()
#     l.append(now)
#     time.sleep(1)
#
#
# random.shuffle(l)
# print(l)
# print(sorted((l)))



# params_list = [
#     {
#         "registration": {
#             1: 'John',
#             2: 'ta',
#             3: 'example1@domain.com'
#         },
#         "confirmation_email": {
#             'enabled': 1,
#             'lang': 'en',
#         }
#     },
#     {
#         "registration": {
#             1: 'John',
#             2: 'taa',
#             3: 'example2@domain.com'
#         },
#         "confirmation_email": {
#             'enabled': 1,
#             'lang': 'en',
#         }
#     },
#     {
#         "registration": {
#             1: 'John',
#             2: 'taaa',
#             3: 'example3@domain.com'
#         },
#         "confirmation_email": {
#             'enabled': 1,
#             'lang': 'en',
#         }
#     },
#
# ]
#
#
#
# load_dotenv(find_dotenv())
#
# client = ClickMeetingRestClient({'api_key': os.getenv('API_KEY')})
#
# for params in params_list:
#     print(client.addConferenceRegistration('7087247', params))

# driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)




options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Runs Chrome in headless mode.
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-gpu')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-application-cache")
options.add_argument('--ignore-certificate-errors')

selenium_hub_url = "http://localhost:4444/wd/hub"
htmlunit_capabilities = DesiredCapabilities.HTMLUNITWITHJS.copy()

driver = webdriver.Remote(
    command_executor=selenium_hub_url,
    options=options,
    desired_capabilities=DesiredCapabilities.CHROME.copy(),

)


driver.get('https://mark533.clickmeeting.com/875445123/6M7HGJ?r=Zwx3AwV0BUk8I2W1LFOaoak8pzghrzA5pwSNpJW6oaMuYaOvrak8AQL5AwZkZwN__')
time.sleep(60)
driver.close()

