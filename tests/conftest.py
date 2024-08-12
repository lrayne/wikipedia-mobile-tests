import allure
import allure_commons
import pytest
from selene import browser, support
from appium import webdriver
from allure import step
from wikipedia_mobile_tests import utils
import settings


@pytest.fixture(scope='function', autouse=True)
def set_up_management():

    with allure.step('Начать сессию'):

        browser.config._wait_decorator = support._logging.wait_with(
            context=allure_commons._allure.StepContext
        )

        if (
            settings.config.context == 'local_real_device'
            or settings.config.context == 'local_emulator'
        ):
            browser.config.driver = webdriver.Remote(
                settings.config.remote_url, options=settings.to_driver_options()
            )

        if settings.config.context == 'bstack':

            browser.config.driver = webdriver.Remote(
                settings.config.remote_url, options=settings.to_driver_options()
            )
            session_id = browser.driver.session_id

    yield

    utils.add_screenshot()
    utils.add_xml()

    if settings.config.context == 'bstack':
        utils.add_video(session_id)

    with step('Завершить сессию'):
        browser.quit()
