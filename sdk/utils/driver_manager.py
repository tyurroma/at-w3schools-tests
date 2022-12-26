from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_chromedriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--incognito')

    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                            desired_capabilities=DesiredCapabilities.CHROME,
                            options=options)
