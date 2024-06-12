from datetime import datetime

from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.SQL.models.base import Base


class GroupOfChannel(Base):
    __tablename__ = 'group_of_channel'

    name: Mapped[str]
    update_at: Mapped[datetime] = mapped_column(server_default=func.now())

    channels: Mapped[list["Channel"]] = relationship(
        "Channel",
        secondary="group_replise",
        back_populates="groups"
    )


class Channel(Base):
    __tablename__ = 'channel'

    link: Mapped[str]

    groups: Mapped[list[GroupOfChannel]] = relationship(
        "GroupOfChannel",
        secondary="group_replise",
        back_populates="channels"
    )


class GroupReplice(Base):
    __tablename__ = 'group_replise'

    group_id: Mapped[int] = mapped_column(ForeignKey("group_of_channel.id",
                                                     ondelete="CASCADE"),
                                          primary_key=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey("channel.id",
                                                       ondelete="CASCADE"),
                                            primary_key=True)
