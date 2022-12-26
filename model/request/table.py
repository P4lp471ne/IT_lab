from typing import List

from pydantic import BaseModel

from model.request.column import Column


class Table(BaseModel):
    name: str = ''
    columns: List[Column] = []
