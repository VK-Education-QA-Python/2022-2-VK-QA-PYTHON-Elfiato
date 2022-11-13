import pytest
from mysql.client import MySqlClient
import utils.scripts as script
from utils.builder import Builder
import models.models as model


class MyTest:
    builder_name = Builder
    model = None

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client: MySqlClient = mysql_client
        self.builder = self.builder_name(client=self.client)
        self.prepare()

    def get_results(self, **filters):
        self.client.session.commit()
        return self.client.session.query(self.model).filter_by(**filters).all()


class TestTotalRequests(MyTest):
    model = model.TotalRequests

    def prepare(self):
        self.builder.add_data(table=self.model, script=script.total_requests)

    def test_total_requests(self):
        requests = self.get_results()
        result = script.total_requests()
        assert len(requests) == 1, f'В таблице "{self.model.__tablename__}" содержится не {len(result)} запись.'
        assert requests[0].amount == result[0], f'Общее число запросов из файла "access.log" отличается от {result}.'


class TestMostFrequentRequests(MyTest):
    model = model.MostFrequentRequests
    amount_of_result = 10

    def prepare(self):
        self.builder.add_data(amount=self.amount_of_result, table=self.model, script=script.most_frequent_requests)

    def test_total_requests(self):
        requests = self.get_results()
        assert len(
            requests) == self.amount_of_result, f'В таблице "{self.model.__tablename__}" содержится не 10 записей.'
        results = script.most_frequent_requests(self.amount_of_result)
        for i in range(len(requests)):
            if requests[i].url != results[i][0] or requests[i].amount != results[i][1]:
                assert False, f'Значение с id - {requests[i].id} из таблицы {self.model.__tablename__} ' \
                              f'не соответствует добавленному ({results[i]}).'


class TestTotalRequestsByType(MyTest):
    model = model.TotalRequestsByType

    def prepare(self):
        self.builder.add_data(table=self.model, script=script.total_requests_by_type)

    def test_total_requests(self):
        requests = self.get_results()
        results = script.total_requests_by_type()
        assert len(requests) == len(
            results), f'В таблице "{self.model.__tablename__}" содержится не {len(results)} записей.'
        for i in range(len(requests)):
            if requests[i].request_type != results[i][0] or requests[i].amount != results[i][1]:
                assert False, f'Значение с id - {requests[i].id} из таблицы {self.model.__tablename__} ' \
                              f'не соответствует добавленному ({results[i]}).'


class TestLargestRequestsThatEndedWithClientError(MyTest):
    model = model.LargestRequestsThatEndedWithClientError
    amount_of_result = 5

    def prepare(self):
        self.builder.add_data(table=self.model, script=script.largest_requests, amount=self.amount_of_result)

    def test_total_requests(self):
        requests = self.get_results()
        results = script.largest_requests(self.amount_of_result)
        assert len(requests) == len(
            results), f'В таблице "{self.model.__tablename__}" содержится не {len(results)} записей.'
        for i in range(len(requests)):
            if requests[i].status != results[i][1] or requests[i].request_size != \
                    results[i][2] or requests[i].ip != results[i][3]:
                assert False, f'Значение с id - {requests[i].id} из таблицы {self.model.__tablename__} ' \
                              f'не соответствует добавленному ({results[i]}).'


class TestUsersWithServerErrorRequests(MyTest):
    model = model.UsersWithServerErrorRequests
    amount_of_result = 5

    def prepare(self):
        self.builder.add_data(table=self.model, script=script.users_with_server_error_requests,
                              amount=self.amount_of_result)

    def test_total_requests(self):
        requests = self.get_results()
        results = script.users_with_server_error_requests(self.amount_of_result)
        assert len(requests) == len(
            results), f'В таблице "{self.model.__tablename__}" содержится не {len(results)} записей.'
        for i in range(len(requests)):
            if requests[i].ip != results[i][0] or requests[i].amount != results[i][1]:
                assert False, f'Значение с id - {requests[i].id} из таблицы {self.model.__tablename__} ' \
                              f'не соответствует добавленному ({results[i]}).'
