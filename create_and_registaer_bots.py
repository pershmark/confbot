import os
import time

import requests
from faker import Faker

from ClickMeetingRestClient import ClickMeetingRestClient
from dotenv import load_dotenv, find_dotenv

from settings import locale

load_dotenv(find_dotenv())


def create_and_registaer_bots(number_of_bots, settings) -> list:
    """
    create and registaer bots in given room
    """

    # api client initialization
    client = ClickMeetingRestClient({'api_key': settings['api_key']['key']})

    try:
        # generate bots
        params_list = []
        for _, bot in zip(range(number_of_bots), settings['bots']):
            params_list.append(
                {
                    "registration": {
                        1: bot['first_name'],
                        2: bot['last_name'],
                        3: bot['email']
                    },
                    "confirmation_email": {
                        'enabled': 1,
                        'lang': 'en',
                    }
                }
            )

        # get authorization links for bots
        urls = []
        for params in params_list:
            res = client.addConferenceRegistration(settings['room_id']['room_id'], params)
            urls.append(res['url'])

        # print(urls)
        return urls

    except Exception as e:
        print(e)
