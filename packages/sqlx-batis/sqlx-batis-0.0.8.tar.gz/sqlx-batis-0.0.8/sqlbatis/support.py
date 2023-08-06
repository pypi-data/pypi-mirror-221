from enum import Enum
# Don't remove. Import for not repetitive implementation
from sqlexec.support import DBError, DB_LOCK


class MapperError(DBError):
    pass


class NotFoundError(DBError):
    pass


class SqlAction(Enum):
    CALL = 'call'
    INSERT = 'insert'
    UPDATE = 'update'
    DELETE = 'delete'
    SELECT = 'select'
