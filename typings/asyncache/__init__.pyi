"""
This type stub file was generated by pyright.
"""

import functools
import inspect
from cachetools import keys
from typing import Any

"""
Helpers to use [cachetools](https://github.com/tkem/cachetools) with
asyncio.
"""

class nullcontext:
    """A class for noop context managers."""

    def __enter__(self):  # -> nullcontext:
        """Return ``self`` upon entering the runtime context."""
        ...
    def __exit__(self, exc_type, exc_value, traceback):  # -> None:
        """Raise any exception triggered within the runtime context."""
        ...
    async def __aenter__(self):  # -> nullcontext:
        """Return ``self`` upon entering the runtime context."""
        ...
    async def __aexit__(self, exc_type, exc_value, traceback):  # -> None:
        """Raise any exception triggered within the runtime context."""
        ...

def cached(
    cache, key=..., lock=...
) -> Any:  # -> (func: Unknown) -> ((*args: Unknown, **kwargs: Unknown) -> Coroutine[Any, Any, Unknown] | (*args: Unknown, **kwargs: Unknown) -> Unknown):
    """
    Decorator to wrap a function or a coroutine with a memoizing callable
    that saves results in a cache.

    When ``lock`` is provided for a standard function, it's expected to
    implement ``__enter__`` and ``__exit__`` that will be used to lock
    the cache when gets updated. If it wraps a coroutine, ``lock``
    must implement ``__aenter__`` and ``__aexit__``.
    """
    ...
