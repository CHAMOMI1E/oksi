from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger

from db.SQL.models.base import Base

bigint = Annotated[int, "BigInteger"]


class Users(Base):
    __tablename__ = 'users'

    id_tg: Mapped[bigint] = mapped_column(BigInteger)
    username: Mapped[str]
