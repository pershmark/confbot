import os
import random
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from get_client import get_client
from bot_commands import command_hello, question_1, question_2
from create_and_registaer_bots import create_and_registaer_bots
from settings import *


load_dotenv(find_dotenv())


if __name__ == '__main__':

    # get number of bots
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

    # get bots
    print(txt_generating_and_connecting_bots)
    urls = create_and_registaer_bots(number_of_bots, os.getenv('ROOM_ID'))
    pool = ThreadPool(10)
    clients = pool.map(get_client, urls)
    pool.close()
    pool.join()

    # commands to bots
    command = input(txt_start_commands)
    while command != 'exit':
        try:
            if command == 'hi':
                command_hello(clients)
            elif command == '1':
                question_1(clients)
            elif command == '2':
                question_2(clients)
            # TODO another commands ...
            command = input(txt_start_commands)
        except Exception as e:
            print(f'ERROR: {e}')
            command = input(txt_start_commands)
            continue
