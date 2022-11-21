from settings import greetings_list, number_of_questions_min, number_of_questions_max, question_1_list, \
    question_2_list
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
        base_command(bot, question_1_list)


def question_2(clients):
    """
    question 2
    :param clients:
    :return:
    """
    for bot in random.sample(clients, k=random.randint(number_of_questions_min, number_of_questions_max)):
        base_command(bot, question_2_list)


def command_hello(clients):
    """
    command hello
    :param clients:
    :return:
    """
    for bot in random.sample(clients, k=random.randint(number_of_questions_min, number_of_questions_max)):
        base_command(bot, greetings_list)
