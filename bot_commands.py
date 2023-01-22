import datetime
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


def base_command(bot, message):
    """
    base command
    """
    try:
        comment_field = bot.find_element(By.NAME, 'message')
        comment_field.send_keys(message)
        comment_field.send_keys(Keys.RETURN)
    except Exception as e:
        with open('log.txt', 'a') as f:  # noqa
            f.write(f'"def base_command": {datetime.datetime.now()}: {e}\n')


def universal_command(clients, command, settings, available_commands=[]):
    if available_commands:
        messages = available_commands[command]
    else:
        messages = command['messages']
    messages = [i['text'] for i in messages]
    for bot in random.sample(clients, k=random.randint(
            settings['general_settings']['number_of_messages_min'],
            settings['general_settings']['number_of_messages_max']
    )):
        base_command(bot, messages.pop())
        time.sleep(random.randint(
            settings['general_settings']['delay_between_messages_min'],
            settings['general_settings']['delay_between_messages_max']
        ))
    return True
