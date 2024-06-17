from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, Column, Text

from db.SQL.models.base import Base

bigint = Annotated[int, "BigInteger"]


class User(Base):
    __tablename__ = 'user'

    id_tg: Mapped[bigint] = mapped_column(BigInteger)
