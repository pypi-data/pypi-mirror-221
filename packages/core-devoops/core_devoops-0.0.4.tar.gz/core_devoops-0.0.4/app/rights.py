"""
Module implementing the sqlmodel orm part of the right table
"""
from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel


if TYPE_CHECKING:
    from app.user import User


class Right(SQLModel, table=True):  # type: ignore
    """
    Simple right class: listing all app_services that a particular user can access to
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    app_service: str
    user_id: Optional[int] = Field(default=None, foreign_key='user.id')
    user: Optional['User'] = Relationship(back_populates='rights')
