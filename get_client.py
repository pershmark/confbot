import os
from multiprocessing.pool import ThreadPool

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from create_and_registaer_bots import create_and_registaer_bots
from settings import number_of_threads


def get_client(url: str) -> webdriver.Chrome:
    """
    get webdriver.Chrome client
    :param url: str
    :return: driver webdriver.Chrome
    """
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-gpu')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path='chromedriver')
    driver.get(url)
    return driver


def create_bots(number_of_bots):
    urls = create_and_registaer_bots(number_of_bots, os.getenv('ROOM_ID'))
    pool = ThreadPool(number_of_threads)
    clients = pool.map(get_client, urls)
    pool.close()
    pool.join()
    return clients


def stop_clients(drivers):
    for driver in drivers:
        driver.quit()