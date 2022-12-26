from entity.column import Column
from entity.database import Database
from entity.table import Table
from service.db_utils import create_db


def create_base_db():
    create_db('base')
    Database.create_table()
    Table.create_table()
    Column.create_table()


if __name__ == '__main__':
    create_base_db()
