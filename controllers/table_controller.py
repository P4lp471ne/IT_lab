from typing import List

from flask import Blueprint, send_file

from model.response.table import Table
from entity.table import Table as TableEntity
from entity.column import Column as ColumnEntity
from service.table_service import TableService

tables_bp = Blueprint('tables', __name__)
table_service = TableService()


@tables_bp.get('/database/<db_name>/table/<table_name>')
def get_table(db_name, table_name):
    """database_database_name_table_get

    Get all tables. # noqa: E501

    :param database_name: Database Name
    :type database_name: str

    :rtype: Union[List[Table], Tuple[List[Table], int], Tuple[List[Table], int, Dict[str, str]]
    """
    return response_from_entity(*table_service.get_table(db_name, table_name))


@tables_bp.post('/database/<db_name>/table')
def create_table():  # noqa: E501
    """database_database_name_table_post

    Create table # noqa: E501

    :param database_name: Database Id
    :type database_name: str
    :param table:
    :type table: dict | bytes

    :rtype: Union[Table, Tuple[Table, int], Tuple[Table, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        table = Table.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


@tables_bp.post('/database/<db_name>/table/<table_name>')
def get_table(database_name, table_name):  # noqa: E501
    """database_database_name_table_table_name_get

    Get table. # noqa: E501

    :param database_name: Database Id
    :type database_name: str

    :rtype: Union[Table, Tuple[Table, int], Tuple[Table, int, Dict[str, str]]
    """
    return response_from_entity(*table_service.get_table(database_name, table_name))


@tables_bp.post('/database/<db_name>/table/<table_name>/data')
def get_table_data(database_name, table_name):  # noqa: E501
    """database_database_name_table_table_name_get

    Get table. # noqa: E501

    :param database_name: Database Id
    :type database_name: str

    :rtype: Union[Table, Tuple[Table, int], Tuple[Table, int, Dict[str, str]]
    """
    return send_file(table_service.get_table_data(database_name, table_name))


@tables_bp.post('/database/<db_name>/table/<table_name>')
def update_table():  # noqa: E501
    """database_database_name_table_table_name_post

    Update table # noqa: E501

    :param database_name: Database Id
    :type database_name: str
    :param table:
    :type table: dict | bytes

    :rtype: Union[Table, Tuple[Table, int], Tuple[Table, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        table = Table.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


@tables_bp.delete('/database/<db_name>/table/<table_name>')
def delete_table(db_name, table_name):
    """database_database_name_table_table_name_delete

    Drop table # noqa: E501

    :param database_name: Database Name
    :type database_name: str
    :param table_name: Table Name
    :type table_name: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return response_from_entity(*table_service.drop_table(db_name, table_name))


def response_from_entity(t: TableEntity, lc: List[ColumnEntity]) -> Table:
    return Table(**{'name': t.name, 'columns': [{'name': col.name, 'col_type': col.type} for col in lc]})
