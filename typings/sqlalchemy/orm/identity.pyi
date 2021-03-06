"""
This type stub file was generated by pyright.
"""

from .. import util

class IdentityMap:
    def __init__(self) -> None:
        ...
    
    def keys(self): # -> KeysView[Unknown]:
        ...
    
    def replace(self, state):
        ...
    
    def add(self, state):
        ...
    
    def update(self, dict_):
        ...
    
    def clear(self):
        ...
    
    def check_modified(self): # -> bool:
        """return True if any InstanceStates present have been marked
        as 'modified'.

        """
        ...
    
    def has_key(self, key): # -> bool:
        ...
    
    def popitem(self):
        ...
    
    def pop(self, key, *args):
        ...
    
    def setdefault(self, key, default=...):
        ...
    
    def __len__(self): # -> int:
        ...
    
    def copy(self):
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def __delitem__(self, key):
        ...
    


class WeakInstanceDict(IdentityMap):
    def __getitem__(self, key):
        ...
    
    def __contains__(self, key): # -> bool:
        ...
    
    def contains_state(self, state): # -> bool:
        ...
    
    def replace(self, state): # -> None:
        ...
    
    def add(self, state): # -> bool:
        ...
    
    def get(self, key, default=...):
        ...
    
    def items(self): # -> list[Unknown]:
        ...
    
    def values(self): # -> list[Unknown]:
        ...
    
    def __iter__(self): # -> Iterator[Unknown]:
        ...
    
    if util.py2k:
        def iteritems(self): # -> Iterator[Unknown]:
            ...
        
        def itervalues(self): # -> Iterator[Unknown]:
            ...
        
    def all_states(self): # -> ValuesView[Unknown] | list[Unknown]:
        ...
    
    def discard(self, state): # -> None:
        ...
    
    def safe_discard(self, state): # -> None:
        ...
    


