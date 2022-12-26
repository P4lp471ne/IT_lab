import json
from typing import List

from pydantic import BaseModel

from model.response.table import Table


class Database(BaseModel, object):
    name: str = ''
    db_id: str = ''
    tables: List[Table] = []

    @classmethod
    def from_json(cls, json_data):
        return Database(**json.loads(json_data))


if __name__ == '__main__':
    print(Database.from_json('''{"name":"1", "tables": [{"name": "1"}]}'''))
