import pytest
from mysql.client import MySqlClient


def pytest_configure(config):
    mysql_client = MySqlClient(user='root', password='pass', db_name='nginx_logs')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()

    mysql_client.connect(db_created=True)

    if not hasattr(config, 'workerinput'):
        mysql_client.create_table('total_request')
        mysql_client.create_table('most_frequent_requests')
        mysql_client.create_table('total_requests_by_type')
        mysql_client.create_table('largest_requests_that_ended_with_client_error')
        mysql_client.create_table('users_with_server_error_requests')

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MySqlClient:
    client: MySqlClient = request.config.mysql_client
    yield client
    client.connection.close()
