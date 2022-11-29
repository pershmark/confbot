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
