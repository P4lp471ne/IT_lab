from typing import Dict

import psycopg2
from jproperties import Properties
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def load_properties():
    with open('../db.properties') as f:
        config.load(f.read())


config = Properties()
load_properties()


def get_connection(database=config.get('dbname').data, user=config.get('user').data,
                   password=config.get('password').data, host='localhost'):
    conn = psycopg2.connect(database=database,
                            user=user,
                            password=password,
                            host=host)
    return conn


def create_table(conn, table_name: str, columns: Dict[str, str]):
    with conn.cursor() as cur:
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{k} {v}' for k, v in columns.items()])})")


def get_table_list(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        return [i[0] for i in cur.fetchall()]


def get_database_list():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT datname FROM pg_database")
        return [i[0] for i in cur.fetchall()]


def get_database_dump(db_id: str):
    ...


def drop_table(conn, table_name: str):
    with conn.cursor() as cur:
        cur.execute(f"drop table {table_name}")


def get_row(conn, table_name, row_id, column_names):
    with conn.get_cursor() as cur:
        cur.execute(f"select {', '.join(column_names)} from {table_name} where id={row_id}")
        return cur.fetchone()


def get_all_rows(conn, table_name, column_names):
    with conn.get_cursor() as cur:
        cur.execute(f"select {', '.join(column_names)} from {table_name}")
        return cur.fetchall()


def add_row(conn, table_name, row: dict):
    with conn.get_cursor() as cur:
        cur.execute(f"insert into {table_name} ({', '.join(row.keys())}) values ({', '.join(row.values())})")


def del_row(conn, table_name, row_id):
    with conn.get_cursor() as cur:
        cur.execute(f"delete from {table_name} where id={row_id}")
        return cur.fetchall()


def update_row(conn, table_name, row_id, row: dict):
    with conn.get_cursor() as cur:
        cur.execute(f"UPDATE {table_name} set {', '.join([f'{k}={v}' for k, v in row])} where id={row_id}")
        return cur.fetchall()


def create_db(db_name):
    connection = get_connection()
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(f"CREATE database {db_name}")
    connection.close()


def drop_db(db_name):
    connection = get_connection()
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(f"DROP database {db_name}")
    connection.close()


if __name__ == '__main__':
    # create_db('example2')
    print(get_database_list())
