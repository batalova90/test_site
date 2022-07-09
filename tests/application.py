from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager import chrome, firefox

from enum_urls import EnumURL


class Application:

    def __init__(self, browser):
        if browser == "firefox":
            self.driver = webdriver.Firefox(
                    executable_path=firefox.GeckoDriverManager().install()
            )
        elif browser == "chrome":
            self.driver = webdriver.Chrome(
                    executable_path=chrome.ChromeDriverManager().install()
            )
        else:
            raise ValueError(f'Unrecognised browser {browser}')

    def teardown_method(self):
        self.driver.quit()

    def open_google_search(self):
        self.driver.get(
                EnumURL.GOOGLE_SEARCH.value
        )

    def find_site(self):
        search_string = self.driver.find_element(
                By.NAME, 'q'
        )
        search_string.send_keys(EnumURL.SEARCH_QUERY.value)
        search_string.send_keys(Keys.ENTER)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False
