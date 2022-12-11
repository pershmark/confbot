import pandas as pd
import requests

file_name = 'commands.xlsx'


def get_data_from_xlsx(file_name):
    df = pd.read_excel(file_name)
    commands = [key for key in df.head().keys()]

    result = {}

    for command in commands:
        lst = df[command].tolist()
        sentences = [x for x in lst if str(x) != 'nan']
        result[str(command)] = sentences

    return result


def get_data_from_web(url):
    response = requests.get(url + '/api/command').json()
    result = {}
    for item in response:
        key = item['name']
        value = item['messages']
        result[key] = value
    return result


def get_timelines(url):
    response = requests.get(url + '/api/timeline').json()
    result = {}
    for item in response:
        key = item['name']
        value = item['commands']
        result[key] = value
    return result


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


