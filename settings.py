import os
from typing import Literal, Optional
import dotenv
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from pydantic_settings import BaseSettings
from wikipedia_mobile_tests import utils

load_dotenv()


class Config(BaseSettings):

    context: Literal['bstack', 'local_real_device', 'local_emulator'] = 'bstack'

    remote_url: str = 'http://hub.browserstack.com/wd/hub'

    platformName: str = 'android'
    platformVersion: Optional[str] = None

    projectName: Optional[str] = None
    buildName: Optional[str] = None
    sessionName: Optional[str] = None

    bstack_userName: str = os.getenv('bstack_username')
    bstack_accessKey: str = os.getenv('bstack_accesskey')

    deviceName: Optional[str] = None
    udid: Optional[str] = None

    timeout: float = 3.0

    app: str = 'app-alpha-universal-release.apk'
    appWaitActivity: str = 'org.wikipedia.*'


config = Config(_env_file=dotenv.find_dotenv(f'config.{Config().context}.env'))


def to_driver_options():
    options = UiAutomator2Options()

    options.set_capability(
        "appWaitActivity",
        config.appWaitActivity,
    )

    if config.context == 'local_real_device' or config.context == 'local_emulator':
        options.set_capability("app", utils.path(config.app))
        options.set_capability("deviceName", config.deviceName)
        options.set_capability("udid", config.udid)

    if config.context == 'bstack':
        options.load_capabilities(
            {
                "app": config.app,
                "deviceName": config.deviceName,
                'bstack:options': {
                    "platformName": config.platformName,
                    "platformVersion": config.platformVersion,
                    "projectName": config.projectName,
                    "buildName": config.buildName,
                    "sessionName": config.sessionName,
                    "userName": config.bstack_userName,
                    "accessKey": config.bstack_accessKey,
                },
            }
        )

    return options
