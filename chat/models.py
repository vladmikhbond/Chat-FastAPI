from pydantic import BaseModel

class Item(BaseModel):
    message: str = ""
    sign: str
    datetime: str 
