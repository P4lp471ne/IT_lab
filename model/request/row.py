from typing import Dict

from pydantic import BaseModel


class Row(BaseModel):
    data: Dict[str, str]
