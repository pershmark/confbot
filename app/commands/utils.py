from ClickMeetingRestClient import ClickMeetingRestClient


def get_room_id(name):
    from commands.models import APIKey
    client = ClickMeetingRestClient({'api_key': APIKey.objects.filter(active=True).first().key})
    conferences = client.conferences('active')
    for conference in conferences:
        try:
            if conference['name'] == name:
                return conference['id']
        except Exception as e:
            print(e)
