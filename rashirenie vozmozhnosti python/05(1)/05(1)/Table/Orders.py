from orm.base_table import BaseTable
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import *
import datetime

class Orders(BaseTable):
    __tablename__ = 'Orders'

    ID: Mapped[BaseTable.type_annotation_map['XXX']]
    Name: Mapped[str]
    Amount: Maped[int]
    CreatedOn: Mapped[datetime.datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP'))
    UpdateAt: Mapped[datetime.datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.datetime.now())

    Products: Mapped['Products'] = relationship(back_populates='Orders')
    print(Orders.__table__.columns)
    OrdersWithFileDTO.model_validate(row, from_attributes=True)

