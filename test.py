import datetime
import random
import time

import requests
from faker import Faker


url = 'http://127.0.0.1:8000'

# API
def get_settings_from_web(url):
    settings = {
        'api_key': requests.get(url + '/api/api_key').json()[0],
        'general_settings': requests.get(url + '/api/general_settings').json()[0],
        'room_id': requests.get(url + '/api/room_id').json()[0],
        'timeline': get_timelines(url),
    }
    resp = requests.get(url + '/api/bots').json()
    bots = []
    for bot in resp:
        if bot['geo'] == settings['general_settings']['geo']:
            bots.append(bot)
    settings['bots'] = bots
    return settings


# settings = get_settings_from_web(url)
# for item in settings.items():
#     print(item)



def get_timelines(url):
    response = requests.get(url + '/api/timeline').json()
    result = {}
    for item in response:
        key = item['name']
        value = item['commands']
        result[key] = value
    return result


l = get_settings_from_web(url)

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
