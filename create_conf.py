import datetime
import os

from dotenv import load_dotenv, find_dotenv

from ClickMeetingRestClient import ClickMeetingRestClient


load_dotenv(find_dotenv())


client = ClickMeetingRestClient({'api_key': os.getenv('API_KEY')})

try:
    room = client.addConference({
        'name': 'test_room',
        'room_type': 'webinar',
        'permanent_room': 1,
        'access_type': 3,
        'lobby_enabled': 1,
        'registration': {
            'enabled': 1
        },
        # 'starts_at': datetime.datetime.now(),
        # 'starts_at': '2022-11-21 15:28:15.450839',
        # 'duration': 10,
        'settings': {
            'show_on_personal_page': 1,
            'thank_you_emails_enabled': 1,
            'connection_tester_enabled': 1,
            'phonegateway_enabled': 1,
            'recorder_autostart_enabled': 1,
            'room_invite_button_enabled': 1,
            'social_media_sharing_enabled': 1,
            'connection_status_enabled': 1,
            # 'thank_you_page_url': 'http://example.com/thank_you.html'
        }
    })

    print(room)
    room_id = room['room']['id']

    print(client.conference(room_id))

    print(client.editConference(room_id, {'name': 'new_test_room'}))

    print(client.conferences('active'))

    params = {
        'email': 'rens2588@gmail.com',
        'nickname': 'mark',
        'role': 'presenter'
    }
    print(client.conferenceAutologinHash(room_id, params))

    params = {"how_many": 2}
    print(client.generateConferenceTokens(room_id, params))

    print(client.conferenceTokens(room_id))

    existing_session_id = 123  # existing session id
    existing_room_id = room_id  # existing room id

    # print(client.conferenceSessions(room_id))

    # # print(client.conferenceSession(existing_room_id, existing_session_id))
    # #
    # # print(client.conferenceSessionAttendees(existing_room_id, existing_session_id))
    # #
    # # print(client.generateConferenceSessionPDF(existing_room_id, existing_session_id, 'en'))

    # params = {
    #     'email': 'example@domain.com',
    #     'firstname': 'John',
    #     'lastname': 'Dee',
    #     'company': 'My company',  # basic / advanced
    #     'country': 'US',
    #     'phone': '+1234567890',
    # }
    #
    # print(client.addContact(params))

    # print(client.timeZoneList())

    # print(client.countryTimeZoneList('us'))
    # #
    # print(client.phoneGatewayList())
    # #
    # # print(client.conferenceSkins())



    # print(client.conferenceRegistrations(room_id, 'all'))




    #
    # print(client.fileLibrary())
    #
    # print(client.conferenceFileLibrary(room_id))
    #
    # file = client.addFileLibraryFile('/my/file.png')
    # print(file)
    # file_id = file["id"]
    #
    # print(client.fileLibraryFile(file_id))
    #
    # print(client.fileLibraryContent(file_id))
    #
    # print(client.deleteFileLibraryFile(file_id))
    #
    # print(client.conferenceRecordings(room_id))
    #
    # print(client.conferenceSessionRegistrations(existing_room_id, existing_session_id, 'all'))
    #
    # print(client.deleteConferenceRecordings(room_id))
    #
    # existing_recording_id = 123
    # print(client.deleteConferenceRecording(existing_room_id, existing_recording_id))
    #
    # print(client.chats())
    #
    # print(client.conferenceSessionChats(existing_session_id))
    #
    # params = {
    #     'attendees': [
    #         {'email': 'example@domain.com'}
    #     ],
    #     'template': 'advanced',  # basic / advanced
    #     'role': 'listener',
    # }
    #
    # print(client.sendConferenceEmailInvitations(room_id, 'us', params))
    #
    # print(client.deleteConference(room_id))



    #
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
    # for params in params_list:
    #     print(client.addConferenceRegistration(room_id, params))


except Exception as e:
    print(e)
