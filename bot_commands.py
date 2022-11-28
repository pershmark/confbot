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


def question_1(clients):
    """
    question 1
    :param clients:
    :return:
    """
    for bot in random.sample(clients, k=random.randint(number_of_questions_min, number_of_questions_max)):
        base_command(bot, available_commands['2'])


def question_2(clients):
    """
    question 2
    :param clients:
    :return:
    """
    for bot in random.sample(clients, k=random.randint(number_of_questions_min, number_of_questions_max)):
        base_command(bot, available_commands['3'])


def command_hello(clients):
    """
    command hello
    :param clients:
    :return:
    """
    for bot in random.sample(clients, k=random.randint(number_of_questions_min, number_of_questions_max)):
        base_command(bot, available_commands['1'])


def universal_command(clients, command):
    for bot in random.sample(clients, k=random.randint(number_of_questions_min, number_of_questions_max)):
        base_command(bot, available_commands[command])


def universal_command_test(clients, command):
    for bot in random.sample(clients, k=random.randint(number_of_questions_min, number_of_questions_max)):
        return f'{bot} says: {available_commands[command][0]}'

