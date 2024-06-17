from datetime import datetime

from sqlalchemy import func, ForeignKey, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.SQL.models.base import Base


class ChatHistory(Base):
    __tablename__ = 'chat_history'

    chat: Mapped[dict] = mapped_column(JSON, nullable=True)
    id_tg: Mapped[int] = ForeignKey('users.id_tg')


class Rule(Base):
    __tablename__ = 'rule'

    text: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
