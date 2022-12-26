from flask import Flask
from peewee import PostgresqlDatabase

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    pg_db = PostgresqlDatabase('postgres', user='postgres', password='password',
                               host='127.0.0.1', port=5432)
    pg_db.connect()
