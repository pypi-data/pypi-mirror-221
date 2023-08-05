"""
Module implementing the sqlmodel orm part of the user table
"""
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from core_devoops.permissions import Permission
if TYPE_CHECKING:
    from core_devoops.app_rights import AppRight


class AppUser(SQLModel, table=True):  # type: ignore
    """
    Simple user class: an id associate to a user with a password
    """
    __tablename__ = 'app_user'
    id: Optional[int] = Field(default=None, primary_key=True)
    user: str = Field(index=True)
    password: str
    permission: Permission = Field(default=Permission.ADMIN)
    client: Optional[str] = Field(default=None)
    rights: List['AppRight'] = Relationship(back_populates='user')
