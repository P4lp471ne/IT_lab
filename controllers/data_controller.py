import connexion


def get_row(database_name, table_name, column_id):  # noqa: E501
    """database_database_name_table_table_name_column_column_id_get

    get column from specified table. # noqa: E501

    :param database_name: Database Id
    :type database_name: str
    :param table_name: Table Id
    :type table_name: str
    :param column_id: Column Id
    :type column_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_row(database_name, table_name, column_id, edit_value_location):  # noqa: E501
    """database_database_name_table_table_name_column_column_id_post

    Update column in specified table. # noqa: E501

    :param database_name: Database Id
    :type database_name: str
    :param table_name: Table Id
    :type table_name: str
    :param column_id: Column Id
    :type column_id: str
    :param edit_value_location:
    :type edit_value_location: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        edit_value_location = EditValueLocation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def database_database_name_table_table_name_column_post(database_name, table_name, row):  # noqa: E501
    """database_database_name_table_table_name_column_post

    Add column to specified table. # noqa: E501

    :param database_name: Database Id
    :type database_name: str
    :param table_name: Table Id
    :type table_name: str
    :param edit_value_location:
    :type edit_value_location: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        edit_value_location = EditValueLocation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
