import pytest
import os

from api.client import ApiClient


def pytest_addoption(parser):
    parser.addoption('--url')


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {
        'url': url,
    }


@pytest.fixture(scope='session')
def api_client(config):
    return ApiClient(base_url=config['url'])
