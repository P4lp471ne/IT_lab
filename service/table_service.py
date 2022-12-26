import re
from io import BytesIO
from typing import List, Tuple

from db_utils import get_connection, create_table, drop_table, get_all_rows
from entity.column import Column as ColumnEntity
from entity.table import Table
from model.request.column import Column
from model.request.table import Table as TableRequest
from service.database_service import get_db

COLUMN_TYPES = ["smallint", "integer", "bigint", "real", "text", "char\([0-9]+\)"]


class TableService:
    def create_table(self, db_name: str, table: TableRequest) -> Tuple[Table, List[ColumnEntity]]:
        db = get_db(db_name)
        self.validate_columns(table.columns)
        self.check_no_tables_with_similar_name(table)
        t = Table(name=table.name, database=db).save()
        columns = [ColumnEntity(col.name, col.col_type, t).save() for col in table.columns]
        create_table(get_connection(db_name), table.name,
                     dict([(column.name, column.col_type) for column in table.columns]))
        return t, columns

    def drop_table(self, db_name: str, table_name: str) -> Tuple[Table, List[ColumnEntity]]:
        db = get_db(db_name)
        table = self.find_table(db, table_name)
        columns = ColumnEntity.select().where(ColumnEntity.table == table)
        Table.delete().where(Table.id == table.id)
        drop_table(get_connection(database=db.name), table_name)

        return table, columns

    @staticmethod
    def find_table(db, table_name) -> Table:
        tables = Table.select().where(Table.name == table_name and Table.database == db)
        tables = [table for table in tables]
        if len(tables) >= 1:
            raise Exception("too many tables")
        elif len(tables) == 0:
            raise Exception("No such table")
        return tables[0]

    def update_table(self, db_id: str, table_id: str, table: TableRequest) -> Table:
        ...

    def get_table(self, db_name: str, table_name: str) -> Tuple[Table, List[ColumnEntity]]:
        db = get_db(db_name)
        table = self.find_table(db, table_name)
        columns = ColumnEntity.select().where(ColumnEntity.table == table)

        return table, columns

    def get_table_data(self, db_name: str, table_name: str):
        db = get_db(db_name)
        table = self.find_table(db, table_name)
        columns = ColumnEntity.select().where(ColumnEntity.table == table)

        return BytesIO(bytes(', '.join(['id'] + [col.name for col in columns]) + '\n' +
                             '\n'.join([', '.join(i) for i in
                                        get_all_rows(db_name, table_name, ['id'] + [col.name for col in columns])])
                             ))

    @staticmethod
    def check_no_tables_with_similar_name(table):
        tables = Table.select(Table.name == table.name)
        tables = [i for i in tables]
        if len(tables) > 0:
            raise "Table with this name already exists"

    @staticmethod
    def validate_columns(columns: List[Column]):
        for column in columns:
            for type in COLUMN_TYPES:
                if re.match(type, column.col_type):
                    break
            else:
                raise Exception(f"wrong type {column.col_type} for column {column.name}")
