from table_data import get_data_from_xlsx, get_data_from_web, get_settings_from_web

# WEB url
web_url = 'http://127.0.0.1:8000'


# main texts
txt_start_commands = 'enter command or timeline to bots (type "/exit" to close the app): '
txt_enter_number_of_bots = 'enter the amount of bots: '
txt_amount_of_bots_must_be_number = 'the amount of bots must be a number'
txt_positive_number = f'the amount of bots must be a positive number'
txt_generating_and_connecting_bots = 'the beginning of the process of generating and connecting bots'
txt_command_not_found = 'command not found'
txt_timeline_not_found = 'timeline not found'
txt_the_process_of_creating_bots = 'the process of creating bots...'
txt_bots_are_created = 'bots created successfully'
txt_command_has_not_been_implemented = 'command has not been implemented'
txt_command_completed_successfully = 'command completed successfully'
txt_create_bots_button = 'Create bots'
txt_stop_bots_button = 'Stop bots'
txt_run_app_button = 'RUN'
txt_broadcast_type = 'choose the type of appearance of messages in the translation:' \
                       ' by command in the chat or by timeline'
txt_command_in_the_chat = 'command_in_chat'
txt_timeline = 'timeline'
txt_exit = 'all bots removed'

# commands
commands_file_name = 'commands.xlsx'


# ways to receive commands and messages (1 or 2 or 3):
way_to_receive_commands_and_messages = 3


def get_available_commands(way_to_receive_commands_and_messages):
    # 3 ways:

    # 1 way: dict in this variable:
    if way_to_receive_commands_and_messages == 1:
        available_commands = {}
        # example:
        # available_commands = {
        #   '1': ['hi', 'hello', 'hey'], '2': ['some sentence 1', 'some sentence 2', 'some sentence 3']
        # }

    # 2 way: get from xlsx file (colum name it is command; rows it is sentences)
    elif way_to_receive_commands_and_messages == 2:
        available_commands = get_data_from_xlsx(commands_file_name)

    # 3 way: get from web server (it is needed to run django app)
    else:
        available_commands = get_data_from_web(web_url)

    return available_commands


def get_settings():
    return get_settings_from_web(web_url)


max_amount_of_bots = 300

number_of_threads = 10



