import os

from dotenv import load_dotenv, find_dotenv

from ClickMeetingRestClient import ClickMeetingRestClient

load_dotenv(find_dotenv())


def register_one(room_id, params):
    client = ClickMeetingRestClient({'api_key': os.getenv('API_KEY')})
    print(client.addConferenceRegistration(room_id, params))


def get_active_conf_info():
    """
    get one active conf and return id
    """
    client = ClickMeetingRestClient({'api_key': os.getenv('API_KEY')})
    conferences = client.conferences('active')
    for conference in conferences:
        try:
            print(conference)
            print(conference['id'])
            print(conference['room_url'])
            print(conference['autologin_hash'])
            print(f"url: {conference['room_url'] + '?l=' + conference['autologin_hash']}")
            print(f"token: {client.conferenceTokens(conference['id'])}")
        except Exception as e:
            print(e)
