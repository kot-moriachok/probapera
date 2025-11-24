from orm.base_table import BaseTable
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import *
import datetime

class Products(BaseTable):
    __tablename__ = 'Products'

    ID: Mapped[BaseTable.type_annotation_map['XXX']]
    Name: Mapped[str]
    Amount: Maped[int]
    CreatedOn: Mapped[datetime.datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP'))
    UpdateAt: Mapped[datetime.datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.datetime.now())

