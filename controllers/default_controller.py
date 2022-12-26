import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.database_create_request import DatabaseCreateRequest  # noqa: E501
from openapi_server.models.database_response import DatabaseResponse  # noqa: E501
from openapi_server.models.edit_value_location import EditValueLocation  # noqa: E501
from openapi_server.models.table import Table  # noqa: E501
from openapi_server import util


def database_database_id_dump_get(database_id):  # noqa: E501
    """database_database_id_dump_get

    Create database dump # noqa: E501

    :param database_id: Database Id
    :type database_id: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    return 'do some magic!'


def database_database_id_get():  # noqa: E501
    """database_database_id_get

    Get database # noqa: E501


    :rtype: Union[DatabaseResponse, Tuple[DatabaseResponse, int], Tuple[DatabaseResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def database_database_id_post(body):  # noqa: E501
    """database_database_id_post

    Update database # noqa: E501

    :param body: 
    :type body: 

    :rtype: Union[DatabaseResponse, Tuple[DatabaseResponse, int], Tuple[DatabaseResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def database_database_id_table_get(database_id):  # noqa: E501
    """database_database_id_table_get

    Get all tables. # noqa: E501

    :param database_id: Database Name
    :type database_id: str

    :rtype: Union[List[Table], Tuple[List[Table], int], Tuple[List[Table], int, Dict[str, str]]
    """
    return 'do some magic!'


def database_database_id_table_post(database_id, table):  # noqa: E501
    """database_database_id_table_post

    Create table # noqa: E501

    :param database_id: Database Id
    :type database_id: str
    :param table: 
    :type table: dict | bytes

    :rtype: Union[Table, Tuple[Table, int], Tuple[Table, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        table = Table.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def database_database_id_table_table_id_column_column_id_get(database_id, table_id, column_id):  # noqa: E501
    """database_database_id_table_table_id_column_column_id_get

    get column from specified table. # noqa: E501

    :param database_id: Database Id
    :type database_id: str
    :param table_id: Table Id
    :type table_id: str
    :param column_id: Column Id
    :type column_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def database_database_id_table_table_id_column_column_id_post(database_id, table_id, column_id, edit_value_location):  # noqa: E501
    """database_database_id_table_table_id_column_column_id_post

    Update column in specified table. # noqa: E501

    :param database_id: Database Id
    :type database_id: str
    :param table_id: Table Id
    :type table_id: str
    :param column_id: Column Id
    :type column_id: str
    :param edit_value_location: 
    :type edit_value_location: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        edit_value_location = EditValueLocation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def database_database_id_table_table_id_column_post(database_id, table_id, edit_value_location):  # noqa: E501
    """database_database_id_table_table_id_column_post

    Add column to specified table. # noqa: E501

    :param database_id: Database Id
    :type database_id: str
    :param table_id: Table Id
    :type table_id: str
    :param edit_value_location: 
    :type edit_value_location: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        edit_value_location = EditValueLocation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def database_database_id_table_table_id_delete(database_id, table_id):  # noqa: E501
    """database_database_id_table_table_id_delete

    Drop table # noqa: E501

    :param database_id: Database Name
    :type database_id: str
    :param table_id: Table Name
    :type table_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def database_database_id_table_table_id_get(database_id):  # noqa: E501
    """database_database_id_table_table_id_get

    Get table. # noqa: E501

    :param database_id: Database Id
    :type database_id: str

    :rtype: Union[Table, Tuple[Table, int], Tuple[Table, int, Dict[str, str]]
    """
    return 'do some magic!'


def database_database_id_table_table_id_post(database_id, table):  # noqa: E501
    """database_database_id_table_table_id_post

    Update table # noqa: E501

    :param database_id: Database Id
    :type database_id: str
    :param table: 
    :type table: dict | bytes

    :rtype: Union[Table, Tuple[Table, int], Tuple[Table, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        table = Table.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def database_from_dump_post(dump=None):  # noqa: E501
    """database_from_dump_post

    Recreate database from dump # noqa: E501

    :param dump: 
    :type dump: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def database_get():  # noqa: E501
    """database_get

    List databases # noqa: E501


    :rtype: Union[List[object], Tuple[List[object], int], Tuple[List[object], int, Dict[str, str]]
    """
    return 'do some magic!'


def database_post(database_create_request):  # noqa: E501
    """database_post

    Create database # noqa: E501

    :param database_create_request: 
    :type database_create_request: dict | bytes

    :rtype: Union[DatabaseResponse, Tuple[DatabaseResponse, int], Tuple[DatabaseResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        database_create_request = DatabaseCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
