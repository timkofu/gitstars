"""
This type stub file was generated by pyright.
"""

import io

py2k = ...
py3k = ...
py36 = ...
is_posix = ...
ArgSpec = ...
def inspect_getargspec(func): # -> ArgSpec:
    """getargspec based on fully vendored getfullargspec from Python 3.3."""
    ...

if py3k:
    ...
else:
    ...
if py3k:
    string_types = ...
    binary_type = ...
    text_type = ...
    def callable(fn): # -> bool:
        ...
    
    def u(s):
        ...
    
    def ue(s):
        ...
    
    range = ...
else:
    string_types = ...
    binary_type = ...
    text_type = ...
    callable = ...
    def u(s):
        ...
    
    def ue(s):
        ...
    
    range = ...
if py3k:
    ...
else:
    ...
if py3k:
    def inspect_formatargspec(args, varargs=..., varkw=..., defaults=..., kwonlyargs=..., kwonlydefaults=..., annotations=..., formatarg=..., formatvarargs=..., formatvarkw=..., formatvalue=..., formatreturns=..., formatannotation=...): # -> str:
        """Copy formatargspec from python 3.7 standard library.

        Python 3 has deprecated formatargspec and requested that Signature
        be used instead, however this requires a full reimplementation
        of formatargspec() in terms of creating Parameter objects and such.
        Instead of introducing all the object-creation overhead and having
        to reinvent from scratch, just copy their compatibility routine.

        """
        ...
    
else:
    ...
if py3k:
    ...
else:
    ...
if py2k:
    ...
if py3k:
    def load_module_py(module_id, path): # -> ModuleType:
        ...
    
    def load_module_pyc(module_id, path): # -> ModuleType:
        ...
    
    def get_bytecode_suffixes(): # -> List[str]:
        ...
    
    def get_current_bytecode_suffixes(): # -> List[str]:
        ...
    
    def has_pep3147(): # -> Literal[True]:
        ...
    
else:
    def load_module_py(module_id, path): # -> ModuleType:
        ...
    
    def load_module_pyc(module_id, path): # -> ModuleType:
        ...
    
    def get_current_bytecode_suffixes(): # -> list[str]:
        ...
    
    def has_pep3147(): # -> Literal[False]:
        ...
    
def with_metaclass(meta, base=...):
    """Create a base class with a metaclass."""
    ...

if py3k:
    def raise_(exception, with_traceback=..., replace_context=..., from_=...): # -> NoReturn:
        r"""implement "raise" with cause support.

        :param exception: exception to raise
        :param with_traceback: will call exception.with_traceback()
        :param replace_context: an as-yet-unsupported feature.  This is
         an exception object which we are "replacing", e.g., it's our
         "cause" but we don't want it printed.    Basically just what
         ``__suppress_context__`` does but we don't want to suppress
         the enclosing context, if any.  So for now we make it the
         cause.
        :param from\_: the cause.  this actually sets the cause and doesn't
         hope to hide it someday.

        """
        ...
    
else:
    ...
class EncodedIO(io.TextIOWrapper):
    def close(self): # -> None:
        ...
    


if py2k:
    class ActLikePy3kIO:
        """Produce an object capable of wrapping either
        sys.stdout (e.g. file) *or* StringIO.StringIO().

        """
        readable = ...
        writable = ...
        closed = ...
        def __init__(self, file_) -> None:
            ...
        
        def write(self, text):
            ...
        
        def flush(self):
            ...
        
    
    
    class EncodedIO(EncodedIO):
        def __init__(self, file_, encoding) -> None:
            ...
        
    
    
