from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR

Base = declarative_base()


class TotalRequests(Base):
    __tablename__ = 'total_request'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'Total requests id={self.id}, amount={self.amount}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)


class MostFrequentRequests(Base):
    __tablename__ = 'most_frequent_requests'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'Most frequent requests id={self.id}, url={self.url}, amount={self.count}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(50), nullable=False)
    amount = Column(Integer, nullable=False)


class TotalRequestsByType(Base):
    __tablename__ = 'total_requests_by_type'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'Total requests by type id={self.id}, request_type={self.request_type}, amount={self.count}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    request_type = Column(VARCHAR(50), nullable=False)
    amount = Column(Integer, nullable=False)


class LargestRequestsThatEndedWithClientError(Base):
    __tablename__ = 'largest_requests_that_ended_with_client_error'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'Largest requests that ended with a client error id={self.id}, url={self.url}, status={self.status}, ' \
               f'request_size={self.request_size}, ip={self.ip}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(300), nullable=False)
    status = Column(Integer, nullable=False)
    request_size = Column(Integer, nullable=False)
    ip = Column(VARCHAR(50), nullable=False)


class UsersWithServerErrorRequests(Base):
    __tablename__ = 'users_with_server_error_requests'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'Users with server error requests id={self.id}, ip={self.ip}, amount={self.amount}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(VARCHAR(50), nullable=False)
    amount = Column(Integer, nullable=False)
