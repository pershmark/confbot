import random

from dotenv import load_dotenv, find_dotenv

from dotenv import load_dotenv, find_dotenv

from bot_commands import universal_command
from get_client import stop_clients, create_bots
from settings import *

load_dotenv(find_dotenv())


if __name__ == '__main__':
    number_of_bots = ''
    while not number_of_bots.isnumeric():
        number_of_bots = input(txt_enter_number_of_bots)
        if not number_of_bots.isnumeric():
            print(txt_amount_of_bots_must_be_number)
        elif number_of_bots.isnumeric() and int(number_of_bots) <= 0:
            print(txt_positive_number)
        else:
            number_of_bots = int(number_of_bots)
            break
        number_of_bots = input(txt_enter_number_of_bots)

    print(txt_the_process_of_creating_bots)
    clients = create_bots(number_of_bots)

    command = input(txt_start_commands)
    while command != 'exit':
        try:
            if command in available_commands.keys():
                try:
                    universal_command(clients, command)
                    command = input(txt_start_commands)
                except Exception as e:
                    print(e)
            elif command == 'exit':
                print(txt_stop_bots_button)
                stop_clients(clients)
                clients = []
                break
            else:
                print(txt_command_not_found)
                command = input(txt_start_commands)
        except Exception as e:
            print(f'ERROR: {e}')
            command = input(txt_start_commands)
            continue

    stop_clients(clients)
