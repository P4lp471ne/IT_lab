from typing import List

from pydantic import BaseModel

from model.response.column import Column


class Table(BaseModel):
    name: str = ''
    columns: List[Column] = []
