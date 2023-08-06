from pydantic import BaseModel


class DictValues(BaseModel):
    category: int
    value: str