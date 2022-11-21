import os
import time

import requests
from faker import Faker

from ClickMeetingRestClient import ClickMeetingRestClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def create_and_registaer_bots(number_of_bots: int, room_id: str) -> list:
    """
    create and registaer bots in given room
    :param number_of_bots: int
    :param room_id: str
    :return: list
    """

    # api client initialization
    client = ClickMeetingRestClient({'api_key': os.getenv('API_KEY')})

    try:
        # generate bots
        fake = Faker()
        params_list = []
        for _ in range(number_of_bots):
            params_list.append(
                {
                    "registration": {
                        1: fake.first_name(),
                        2: fake.last_name(),
                        3: fake.email()
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
            res = client.addConferenceRegistration(room_id, params)
            urls.append(res['url'])

        # print(urls)
        return urls

    except Exception as e:
        print(e)
