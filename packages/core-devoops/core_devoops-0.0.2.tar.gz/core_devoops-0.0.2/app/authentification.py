"""
Module implementing all jwt security logic
"""
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Dict
from typing import List
from typing import Union

from app.user import User
from app.logger import logger_get
from app.db_connection import engine
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from jose import jwt
from passlib.context import CryptContext
from sqlmodel import Session
from sqlmodel import col
from sqlmodel import select

from app.auth_configuration import AUTH
from app.pydantic_utils import Frozen


SCHEME = OAuth2PasswordBearer(tokenUrl='login')
auth_router = APIRouter(tags=['authentication'])
CONTEXT = CryptContext(schemes=['bcrypt'], deprecated='auto')
log = logger_get(__name__)


class Token(Frozen):
    """
    Simple class for storing token value and type
    """
    access_token: str
    token_type: str


class TokenData(Frozen):
    """
    Simple class storing token id information
    """
    id: int


def get_app_services(user: User, session: Session) -> List[str]:
    """
    Retrieve all app services the passed user has access to
    """
    if db_user :=  session.exec(select(User).where(col(User.id) == user.id)).first():
        return [right.app_service for right in db_user.rights]
    return []


def attempt_to_log(user: str,
                   password: str,
                   session: Session):
    """
    Factorized security logic. Ensure that the user is a legit one with a valid password
    """
    selector = select(User).where(col(User.user) == user)
    if not (db_user := session.exec(selector).first()):
        log.warning('unauthorized user')
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid Credentials')
    if not _check_password(password, db_user.password):
        log.warning('invalid user')
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid Credentials')

    return {'access_token': _create_access_token(data={'user_id': db_user.id}),
            'token_type': 'bearer'}


def get_current_user(token: str) -> Union[User, None]:
    """
    Retrieves (if it exists) a valid (meaning who has valid credentials) user from the db
    """
    token = _verify_access_token(token)
    with Session(engine) as session:
        return session.exec(select(User).where(col(User.id) == token.id)).first()


def is_admin_user(token: str = Depends(SCHEME)) -> Union[bool, None]:
    """
    Retrieves (if it exists) the admin (meaning who has valid credentials) user from the db
    """
    if (user := get_current_user(token)) and user.user == AUTH.admin_user:
        return True
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='Could not validate credentials. You need admin rights to call this',
                        headers={'WWW-Authenticate': 'Bearer'})


def _create_access_token(data: Dict) -> str:
    """
    Create an access token out of the passed data. Only called if credentials are valid
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=AUTH.access_token_expire_minutes)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, AUTH.secret_key, algorithm=AUTH.algorithm)


def _verify_access_token(token: str) -> TokenData:
    """
    Retrieves the token data associated to the passed token if it contains valid credential info.
    """
    try:
        payload = jwt.decode(token, AUTH.secret_key, algorithms=[AUTH.algorithm])
        if (user_id := payload.get('user_id')) is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate credentials',
                                headers={'WWW-Authenticate': 'Bearer'})
        return TokenData(id=user_id)
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate credentials',
                            headers={'WWW-Authenticate': 'Bearer'}) from e


def _hash_password(password: str) -> str:
    """
    Hashes the passed password (encoding).
    """
    return CONTEXT.hash(password)


def _check_password(plain_password: str, hashed_password: str) -> str:
    """
    Check the passed password (compare it to the passed encoded one).
    """
    return CONTEXT.verify(plain_password, hashed_password)
