import pytest
from mysql.client import MySqlClient


def pytest_configure(config):
    mysql_client = MySqlClient(user='root', password='pass', db_name='nginx_logs')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()

    mysql_client.connect(db_created=True)
    tables = ['total_request', 'most_frequent_requests', 'total_requests_by_type',
              'largest_requests_that_ended_with_client_error', 'users_with_server_error_requests']
    if not hasattr(config, 'workerinput'):
        for table in tables:
            mysql_client.create_table(table)
    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MySqlClient:
    client: MySqlClient = request.config.mysql_client
    yield client
    client.connection.close()
