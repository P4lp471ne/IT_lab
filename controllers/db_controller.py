from typing import List, Tuple

import connexion
from flask import Blueprint, send_file

from model.response.database import Database
from openapi_server.models import DatabaseCreateRequest
from service.database_service import DatabaseService

from entity.database import Database as DatabaseEntity
from entity.table import Table as TableEntity
from entity.column import Column as ColumnEntity

databases_bp = Blueprint('databases', __name__)

database_service = DatabaseService()


@databases_bp.get('/database/<db_name>/dump')
def load_dump():
    """database_database_id_dump_get

    Create database dump # noqa: E501

    :param database_id: Database Id
    :type database_id: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    return 'do some magic!'


@databases_bp.get('/database/<db_name>')
def get_database():  # noqa: E501
    """database_database_id_get

    Get database # noqa: E501


    :rtype: Union[DatabaseResponse, Tuple[DatabaseResponse, int], Tuple[DatabaseResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


@databases_bp.post('/database/<db_name>/dump')
def database_from_dump(dump=None):  # noqa: E501
    """database_from_dump_post

    Recreate database from dump # noqa: E501

    :param dump:
    :type dump: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    return 'do some magic!'


@databases_bp.get('/database')
def list_databases():  # noqa: E501
    """database_get

    List databases # noqa: E501


    :rtype: Union[List[object], Tuple[List[object], int], Tuple[List[object], int, Dict[str, str]]
    """
    return [response_from_entity(d, lt) for d, lt in database_service.get_all_databases()]


@databases_bp.post('/database')
def create_database():  # noqa: E501
    """database_post

    Create database # noqa: E501

    :param database_create_request:
    :type database_create_request: dict | bytes

    :rtype: Union[DatabaseResponse, Tuple[DatabaseResponse, int], Tuple[DatabaseResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        database_create_request = DatabaseCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def response_from_entity(d: DatabaseEntity, lt: List[Tuple[TableEntity, List[ColumnEntity]]]) -> Database:
    return Database(
        **{
            'name': d.name,
            'tables': [
                {'name': t[0].name, 'columns': [{'name': col.name, 'col_type': col.type} for col in t[1]]} for t in lt
            ]
        }
    )
