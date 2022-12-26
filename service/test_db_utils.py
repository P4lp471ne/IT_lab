import random
import string

from service.db_utils import *


def get_random_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


db_name1 = get_random_name()
db_name2 = get_random_name()


def test_create_db():
    create_db(db_name1)
    create_db(db_name2)

    assert db_name1 in get_database_list()
    assert db_name2 in get_database_list()

    drop_db(db_name1)
    drop_db(db_name2)


def test_drop_db():
    create_db(db_name1)
    create_db(db_name2)
    drop_db(db_name1)
    drop_db(db_name2)

    assert db_name1 not in get_database_list()
    assert db_name2 not in get_database_list()


def test_create_table():
    conn = get_connection()
    table_name = get_random_name()
    columns = {'a': 'integer', 'b': 'real'}
    create_table(conn, table_name=table_name, columns=columns)

    assert False


def test_drop_table():
    assert False


def test_update_row():
    assert False


def test_del_row():
    assert False


def test_add_row():
    assert False


def test_get_row():
    assert False


def test_get_database_dump():
    assert False


def test_get_database_list():
    assert False


def test_get_table_list():
    assert False


def test_get_connection():
    assert False
