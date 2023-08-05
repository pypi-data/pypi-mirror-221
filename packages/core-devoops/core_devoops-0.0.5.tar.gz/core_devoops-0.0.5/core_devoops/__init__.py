"""
Module listing all public method from the core_devoops modules
"""

from core_devoops.authentification import Token, get_app_services, attempt_to_log, get_current_user, \
    is_admin_user
from core_devoops.check_dependencies import compute_dependencies
from core_devoops.db_connection import engine, get_session, info_message, create_db_and_tables, delete_table
from core_devoops.list_utils import first_or_default, group_by_value, lselect, lselectfirst, \
    first_transformed_or_default
from core_devoops.logger import logger_get, log_critical
from core_devoops.permissions import Permission
from core_devoops.pydantic_utils import Basic, CustomFrozen, Frozen, OrmFrozen

from core_devoops.read_write import write_json_file, load_json_file, make_dir
from core_devoops.rights import Right
from core_devoops.safe_utils import SafeTestCase, SimpleReturn, safe_clt, stringify, boolify, intify, \
    floatify

from core_devoops.user import User

from core_devoops.auth_configuration import AUTH


__all__ = [
    'AUTH', 'Token', 'get_app_services', 'attempt_to_log', 'get_current_user', 'is_admin_user',
    'write_json_file', 'load_json_file', 'make_dir', 'check_dependencies', 'compute_dependencies',
    'engine', 'create_db_and_tables', 'get_session', 'info_message', 'group_by_value',
    'first_or_default', 'lselect', 'lselectfirst', 'first_transformed_or_default', 'log_critical',
    'logger_get', 'Permission', 'User', 'Right', 'Basic', 'Frozen', 'CustomFrozen', 'OrmFrozen',
    'SafeTestCase', 'SimpleReturn', 'safe_clt', 'stringify', 'boolify', 'intify', 'floatify',
    'delete_table'
]
