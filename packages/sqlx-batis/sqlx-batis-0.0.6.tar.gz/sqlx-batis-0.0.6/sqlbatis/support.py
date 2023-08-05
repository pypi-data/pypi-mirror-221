from enum import Enum
from sqlexec.support import DBError


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
