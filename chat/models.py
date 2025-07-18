# from pydantic import BaseModel

# class Item(BaseModel):
#     id: int
#     message: str = ""
#     sign: str
#     datetime: str 

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Item(Base):
   __tablename__ = "items"
   id: Mapped[int] = mapped_column(primary_key=True)
   message: Mapped[str] = mapped_column()
   sign: Mapped[str] = mapped_column(String(30))
   datetime: Mapped[str] = mapped_column(String(50))