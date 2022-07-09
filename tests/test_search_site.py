from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from enum_urls import EnumInfo, EnumURL


def test_open_site(app):
    app.open_google_search()
    app.find_site()

    get_first_link = app.driver.find_element(
            By.CSS_SELECTOR,
            "div:nth-child(1) > .g > div > div .LC20lb"
    ).click()

    new_window = app.driver.window_handles[1]
    app.driver.switch_to.window(new_window)
    assert app.driver.current_url == EnumURL.TEST_SITE.value, "Another site opened!"

    contact_window = WebDriverWait(app.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                ".btn--lg"))
    ).click()

    contact_info = []
    contact_info = app.driver.find_elements(
            By.CSS_SELECTOR,
            "div.popup-callback__footer-contacts a"
    )
    assert contact_info[0].text == EnumInfo.NUMBER.value, "The number doesn't match!"

    assert contact_info[1].text == EnumInfo.EMAIL.value, "The email doesn't match!"
