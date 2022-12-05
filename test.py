import requests
from faker import Faker


url = 'http://127.0.0.1:8000'


def get_settings_from_web(url):
    settings = {
        'api_key': requests.get(url + '/api/api_key').json()[0],
        'general_settings': requests.get(url + '/api/general_settings').json()[0],
        'room_id': requests.get(url + '/api/room_id').json()[0],
    }
    resp = requests.get(url + '/api/bots').json()
    bots = []
    for bot in resp:
        if bot['geo'] == settings['general_settings']['geo']:
            bots.append(bot)
    settings['bots'] = bots
    return settings


number_of_bots = 100

settings = get_settings_from_web(url)

for item in settings.items():
    print(item)



