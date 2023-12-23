import logging

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class YandexSearchLocators:
    """
    Yandex-page locators
    """
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_RESULT = (By.CSS_SELECTOR, "ul#search-result")


class PageHelper:
    """
    Helper for work with elements
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        logging.info(f"Find element {locator}")
        print(f"Find element {locator}")
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


class WebDriverHelper:
    """
    Helper for work with WebDriver
    """

    def __init__(self, url):
        service = Service('chromedriver.exe')
        browser = webdriver.Chrome(service=service)
        browser.set_page_load_timeout(30)
        logging.info(f"Open url {url}")
        print(f"Open url {url}")
        browser.get(url)
        self.driver = browser

    def get_driver(self):
        return self.driver

    def end_driver(self):
        self.driver.save_screenshot('screen.png')
        self.driver.quit()


def test():
    """
    Test with YandexSearch
    """
    browser = WebDriverHelper('https://ya.ru/')
    search_input = PageHelper(browser.get_driver()).find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
    search_text = 'AT QA' + Keys.ENTER
    logging.info(f"Input search text: {search_text}")
    print(f"Input search text: {search_text}")
    search_input.send_keys(search_text)

    PageHelper(browser.get_driver()).find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULT)
    browser.end_driver()
