"""
This type stub file was generated by pyright.
"""

class SchemaObjects:
    def __init__(self, migration_context=...) -> None:
        ...
    
    def primary_key_constraint(self, name, table_name, cols, schema=...):
        ...
    
    def foreign_key_constraint(self, name, source, referent, local_cols, remote_cols, onupdate=..., ondelete=..., deferrable=..., source_schema=..., referent_schema=..., initially=..., match=..., **dialect_kw):
        ...
    
    def unique_constraint(self, name, source, local_cols, schema=..., **kw):
        ...
    
    def check_constraint(self, name, source, condition, schema=..., **kw):
        ...
    
    def generic_constraint(self, name, table_name, type_, schema=..., **kw):
        ...
    
    def metadata(self):
        ...
    
    def table(self, name, *columns, **kw):
        ...
    
    def column(self, name, type_, **kw):
        ...
    
    def index(self, name, tablename, columns, schema=..., **kw):
        ...
    


