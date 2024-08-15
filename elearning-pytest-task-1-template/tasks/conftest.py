import pytest
import sqlite3

table_data = [(1, "books")]


@pytest.fixture(scope='session')
def connection():
    connection = sqlite3.connect('example.db')
    yield connection
    connection.close()


@pytest.fixture(scope='session')
def cursor(connection):
    cursor = connection.cursor()
    return cursor


@pytest.fixture(scope='function', params=table_data)
def table_cursor(request, cursor):
    cursor.execute('drop table if exists items')
    cursor.execute('create table items (id int, name text)')
    cursor.execute(f'insert into items values {request.param}')
    cursor.connection.commit()
    yield cursor
    cursor.execute('drop table if exists items')

