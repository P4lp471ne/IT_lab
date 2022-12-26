from peewee import PostgresqlDatabase
from service.db_utils import config

db = PostgresqlDatabase(config.get('bas_db_name').data, user=config.get('user').data,
                        password=config.get('password').data, host='localhost', port=5432)
db.connect()
