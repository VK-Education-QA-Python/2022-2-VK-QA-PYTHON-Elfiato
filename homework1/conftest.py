import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--headless", action='store_true')


@pytest.fixture()
def config(request):
    headless = request.config.getoption('--headless')
    return {'headless': headless}


@pytest.fixture(scope='function')
def driver(config):
    options = Options()
    if config['headless']:
        options.add_argument("--headless")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("user-agent=Chrome/105.0.5195.19")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version='105.0.5195.19').install()),
                              options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
