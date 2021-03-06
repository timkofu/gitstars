"""
This type stub file was generated by pyright.
"""

from ..util.compat import with_metaclass

class ImplMeta(type):
    def __init__(cls, classname, bases, dict_) -> None:
        ...
    


_impls = ...
Params = ...
class DefaultImpl(with_metaclass(ImplMeta)):
    """Provide the entrypoint for major migration operations,
    including database-specific behavioral variances.

    While individual SQL/DDL constructs already provide
    for database-specific implementations, variances here
    allow for entirely different sequences of operations
    to take place for a particular migration, such as
    SQL Server's special 'IDENTITY INSERT' step for
    bulk inserts.

    """
    __dialect__ = ...
    transactional_ddl = ...
    command_terminator = ...
    type_synonyms = ...
    type_arg_extract = ...
    identity_attrs_ignore = ...
    def __init__(self, dialect, connection, as_sql, transactional_ddl, output_buffer, context_opts) -> None:
        ...
    
    @classmethod
    def get_by_dialect(cls, dialect):
        ...
    
    def static_output(self, text): # -> None:
        ...
    
    def requires_recreate_in_batch(self, batch_op): # -> Literal[False]:
        """Return True if the given :class:`.BatchOperationsImpl`
        would need the table to be recreated and copied in order to
        proceed.

        Normally, only returns True on SQLite when operations other
        than add_column are present.

        """
        ...
    
    def prep_table_for_batch(self, batch_impl, table): # -> None:
        """perform any operations needed on a table before a new
        one is created to replace it in batch mode.

        the PG dialect uses this to drop constraints on the table
        before the new one uses those same names.

        """
        ...
    
    @property
    def bind(self):
        ...
    
    def execute(self, sql, execution_options=...): # -> None:
        ...
    
    def alter_column(self, table_name, column_name, nullable=..., server_default=..., name=..., type_=..., schema=..., autoincrement=..., comment=..., existing_comment=..., existing_type=..., existing_server_default=..., existing_nullable=..., existing_autoincrement=...): # -> None:
        ...
    
    def add_column(self, table_name, column, schema=...): # -> None:
        ...
    
    def drop_column(self, table_name, column, schema=..., **kw): # -> None:
        ...
    
    def add_constraint(self, const): # -> None:
        ...
    
    def drop_constraint(self, const): # -> None:
        ...
    
    def rename_table(self, old_table_name, new_table_name, schema=...): # -> None:
        ...
    
    def create_table(self, table): # -> None:
        ...
    
    def drop_table(self, table): # -> None:
        ...
    
    def create_index(self, index): # -> None:
        ...
    
    def create_table_comment(self, table): # -> None:
        ...
    
    def drop_table_comment(self, table): # -> None:
        ...
    
    def create_column_comment(self, column): # -> None:
        ...
    
    def drop_index(self, index): # -> None:
        ...
    
    def bulk_insert(self, table, rows, multiinsert=...): # -> None:
        ...
    
    def compare_type(self, inspector_column, metadata_column): # -> bool:
        """Returns True if there ARE differences between the types of the two
        columns. Takes impl.type_synonyms into account between retrospected
        and metadata types
        """
        ...
    
    def compare_server_default(self, inspector_column, metadata_column, rendered_metadata_default, rendered_inspector_default):
        ...
    
    def correct_for_autogen_constraints(self, conn_uniques, conn_indexes, metadata_unique_constraints, metadata_indexes): # -> None:
        ...
    
    def cast_for_batch_migrate(self, existing, existing_transfer, new_type): # -> None:
        ...
    
    def render_ddl_sql_expr(self, expr, is_server_default=..., **kw):
        """Render a SQL expression that is typically a server default,
        index expression, etc.

        .. versionadded:: 1.0.11

        """
        ...
    
    def correct_for_autogen_foreignkeys(self, conn_fks, metadata_fks): # -> None:
        ...
    
    def autogen_column_reflect(self, inspector, table, column_info): # -> None:
        """A hook that is attached to the 'column_reflect' event for when
        a Table is reflected from the database during the autogenerate
        process.

        Dialects can elect to modify the information gathered here.

        """
        ...
    
    def start_migrations(self): # -> None:
        """A hook called when :meth:`.EnvironmentContext.run_migrations`
        is called.

        Implementations can set up per-migration-run state here.

        """
        ...
    
    def emit_begin(self): # -> None:
        """Emit the string ``BEGIN``, or the backend-specific
        equivalent, on the current connection context.

        This is used in offline mode and typically
        via :meth:`.EnvironmentContext.begin_transaction`.

        """
        ...
    
    def emit_commit(self): # -> None:
        """Emit the string ``COMMIT``, or the backend-specific
        equivalent, on the current connection context.

        This is used in offline mode and typically
        via :meth:`.EnvironmentContext.begin_transaction`.

        """
        ...
    
    def render_type(self, type_obj, autogen_context): # -> Literal[False]:
        ...
    


