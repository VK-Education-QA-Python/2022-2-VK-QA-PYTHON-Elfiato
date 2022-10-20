import os
import shutil
import sys
import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.main_page import MainPage

from filelock import FileLock


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerunput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_temp_dir = base_dir


@pytest.fixture()
def driver(config, temp_dir):
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": temp_dir})
    user_agent = ('chrome', '105.0.5195.19')
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '105.0.5195.19',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    else:
        if config['headless']:
            options.add_argument("--headless")
        # options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f"user-agent=Chrome/{user_agent[1]}")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version=f'{user_agent[1]}').install()),
                                  options=options)
    driver.get(url)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("user-agent=Chrome/105.0.5195.19")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version='105.0.5195.19').install()),
                              options=options)
    driver.set_window_size(1920, 1080)
    return driver


def cookies(config):
    driver = get_driver()
    driver.get(config['url'])
    main_page = MainPage(driver)
    login_page = main_page.go_to_login_page()
    dashboard_page = login_page.login()
    dashboard_page.is_user_name_button_present()
    cookies = driver.get_cookies()
    driver.quit()
    return cookies


@pytest.fixture(scope='session')
def get_cookies(tmp_path_factory, worker_id, config):
    if not worker_id:
        return cookies(config)

    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = cookies(config)
            fn.write_text(json.dumps(data))
    return data
