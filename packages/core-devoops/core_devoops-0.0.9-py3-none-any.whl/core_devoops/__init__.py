"""
Module listing all public method from the core_devoops modules
"""
from core_devoops.auth_configuration import AUTH
from core_devoops.authentification import attempt_to_log
from core_devoops.authentification import get_app_services
from core_devoops.authentification import get_current_user
from core_devoops.authentification import is_admin_user
from core_devoops.authentification import SCHEME
from core_devoops.authentification import Token
from core_devoops.check_dependencies import compute_dependencies
from core_devoops.db_connection import create_db_and_tables
from core_devoops.db_connection import DB_URL
from core_devoops.db_connection import delete_table
from core_devoops.db_connection import engine
from core_devoops.db_connection import get_session
from core_devoops.db_connection import info_message
from core_devoops.list_utils import first_or_default
from core_devoops.list_utils import first_transformed_or_default
from core_devoops.list_utils import group_by_value
from core_devoops.list_utils import lselect
from core_devoops.list_utils import lselectfirst
from core_devoops.logger import log_critical
from core_devoops.logger import logger_get
from core_devoops.pandas_utils import pd_equals, jsonify_series
from core_devoops.permissions import Permission
from core_devoops.pydantic_utils import Basic
from core_devoops.pydantic_utils import CustomFrozen
from core_devoops.pydantic_utils import Frozen
from core_devoops.pydantic_utils import OrmFrozen
from core_devoops.read_write import load_json_file
from core_devoops.read_write import make_dir
from core_devoops.read_write import write_json_file
from core_devoops.rights import Right
from core_devoops.safe_utils import boolify
from core_devoops.safe_utils import floatify
from core_devoops.safe_utils import intify
from core_devoops.safe_utils import safe_clt
from core_devoops.safe_utils import SafeTestCase
from core_devoops.safe_utils import SimpleReturn
from core_devoops.safe_utils import stringify
from core_devoops.user import User


__all__ = [
    'AUTH', 'Token', 'get_app_services', 'attempt_to_log', 'get_current_user', 'is_admin_user',
    'write_json_file', 'load_json_file', 'make_dir', 'check_dependencies', 'compute_dependencies',
    'engine', 'create_db_and_tables', 'get_session', 'info_message', 'group_by_value',
    'first_or_default', 'lselect', 'lselectfirst', 'first_transformed_or_default', 'log_critical',
    'logger_get', 'Permission', 'User', 'Right', 'Basic', 'Frozen', 'CustomFrozen', 'OrmFrozen',
    'SafeTestCase', 'SimpleReturn', 'safe_clt', 'stringify', 'boolify', 'intify', 'floatify',
    'delete_table', 'SCHEME', 'DB_URL', 'pd_equals', 'jsonify_series'
]
