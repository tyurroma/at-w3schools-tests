from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_chromedriver():
    options = webdriver.ChromeOptions()

    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    return webdriver.Chrome(executable_path='resources/chromedriver', options=options)
    # return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
    #                         options=options)
