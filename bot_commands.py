import time

from settings import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def base_command(bot, commands_list):
    """
    base command
    :param bot:
    :param commands_list:
    :return:
    """
    comment_field = bot.find_element(By.NAME, 'message')
    comment_field.send_keys(random.choice(commands_list))
    comment_field.send_keys(Keys.RETURN)


def universal_command(clients, command, available_commands, settings):
    for bot in random.sample(clients, k=random.randint(
            settings['general_settings']['number_of_messages_min'],
            settings['general_settings']['number_of_messages_max']
    )):
        base_command(bot, available_commands[command])
        time.sleep(random.randint(
            settings['general_settings']['delay_between_messages_min'],
            settings['general_settings']['delay_between_messages_max']
        ))
    return True


def universal_command_test(clients, command, available_commands):
    for bot in random.sample(clients, k=random.randint(number_of_questions_min, number_of_questions_max)):
        return f'{bot} says: {available_commands[command][0]}'

