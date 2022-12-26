from pydantic import BaseModel


class Column(BaseModel):
    name: str = ''
    col_type: str = ''
