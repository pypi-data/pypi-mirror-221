"""
Module implementing the sqlmodel orm part of the user table
"""
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from app.permissions import Permission

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel
if TYPE_CHECKING:
    from app.rights import Right


class User(SQLModel, table=True):  # type: ignore
    """
    Simple user class: an id associate to a user with a password
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user: str = Field(index=True)
    password: str
    permission: Permission = Field(default=Permission.ADMIN)
    client: Optional[str] = Field(default=None)
    rights: List['Right'] = Relationship(back_populates='user')
