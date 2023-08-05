import sqlexec
from . import DBEngin
from .sql_holder import do_get_sql
from .support import SqlAction, DBError


def do_save(sql_model, batch, param_names, *args, **kwargs):
    assert SqlAction.INSERT.value == sql_model.action, 'Only insert sql can return primary key.'
    sql, args = do_get_sql(sql_model, batch, param_names, *args, **kwargs)
    select_key = sql_model.select_key
    pk_seq = sql_model.pk_seq
    return  do_save0(select_key, pk_seq, sql, *args)


def do_save0(select_key, pk_seq, sql, *args):
    if select_key:
        return sqlexec.save_sql(select_key, sql, *args)

    select_key = DBEngin.get_select_key(pk_seq=pk_seq, sql=sql)
    if select_key:
        return sqlexec.save_sql(select_key, sql, *args)

    raise DBError("Can not get select key.")
