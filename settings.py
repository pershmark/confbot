from table_data import get_data_from_xlsx, get_data_from_web

# https://faker.readthedocs.io/en/master/locales.html
# locale = 'en'
locale = 'ru_RU'

max_amount_of_bots = 300

number_of_threads = 10

# main texts
txt_start_commands = 'enter command to bots (type "exit" to close the app): '
txt_enter_number_of_bots = 'enter the amount of bots: '
txt_amount_of_bots_must_be_number = 'the amount of bots must be a number'
txt_positive_number = f'the amount of bots must be a positive number but not bigger than {max_amount_of_bots}'
txt_generating_and_connecting_bots = 'the beginning of the process of generating and connecting bots'
txt_command_not_found = 'command not found'
txt_the_process_of_creating_bots = 'the process of creating bots...'
txt_bots_are_created = 'bots created successfully'
txt_exit = 'do you want to exit?'
txt_command_has_not_been_implemented = 'command has not been implemented'
txt_command_completed_successfully = 'command completed successfully'
txt_create_bots_button = 'Create bots'
txt_stop_bots_button = 'Stop bots'
txt_run_app_button = 'RUN'

# random amount of question
number_of_questions_min = 2
number_of_questions_max = 5

# commands
commands_file_name = 'commands.xlsx'

# WEB url
web_url = 'http://127.0.0.1:8000'


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
