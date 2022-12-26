from model.request.row import Row
from service.database_service import get_db
from service.table_service import TableService
from db_utils import add_row, del_row, update_row, get_row, get_connection


class DataService:
    def __init__(self):
        self.table_service = TableService()

    def get_row(self, db_name, db_table, row_id) -> Row:
        db = get_db(db_name)
        table, columns = self.table_service.get_table(db, db_table)

        return get_row(get_connection(db.name), table.name, row_id, [col.name for col in columns])

    def add_row(self, db_name, db_table, row: Row) -> Row:
        db = get_db(db_name)
        table = TableService.find_table(db, db_table)
        return add_row(get_connection(db.name), table.name, row.data)  ## todo validate

    def del_row(self, db_name, db_table, row_id) -> Row:
        db = get_db(db_name)
        table = TableService.find_table(db, db_table)
        return del_row(get_connection(db.name), table.name, row_id)

    def update_row(self, db_name, db_table, row: Row) -> Row:
        db = get_db(db_name)
        table = TableService.find_table(db, db_table)
        return update_row(get_connection(db.name), table.name, row.data)  ## todo validate
