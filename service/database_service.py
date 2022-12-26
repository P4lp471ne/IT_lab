from entity.column import Column
from entity.table import Table
from model.request.database import Database as DatabaseRequest
from entity.database import Database
from service.db_utils import create_db, drop_db
from service.table_service import TableService


class DatabaseService:
    def __init__(self):
        self.table_service = TableService()

    def get_database(self, db_name):
        db = get_db(db_name)
        tables = Table.select().where(Table.database == db)
        tables_full = [self.table_service.get_table(db_name, i.name) for i in tables]
        return db, tables_full

    def create_database(self, database: DatabaseRequest):
        de = Database(name=database.name)
        create_db(de.name)
        for table in database.tables:
            self.table_service.create_table(de.name, table)
        return self.get_database(database.name)

    @staticmethod
    def delete_database(self, db_name: str):
        db = self.get_database(db_name)
        Column.delete().where(Column.table.in_([i[0] for i in db[1]]))
        Table.delete().where(Table.database == db[0])
        Database.delete().where(Database.id == db[0].id)
        drop_db(db_name)
        return db

    def get_all_databases(self):
        return [self.get_database(db.name) for db in Database.select()]


def get_db(db_name) -> Database:
    db_request_res = Database.select().where(Database.name == db_name)
    db = [i for i in db_request_res]
    if len(db) >= 1:
        raise Exception("too many db's")
    elif len(db) == 0:
        raise Exception("No such db")
    db = db[0]
    return db
