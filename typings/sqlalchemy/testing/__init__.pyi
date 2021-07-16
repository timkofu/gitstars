"""
This type stub file was generated by pyright.
"""

from . import config, mock
from .assertions import AssertsCompiledSQL, AssertsExecutionResults, ComparesTables, assert_raises, assert_raises_context_ok, assert_raises_message, assert_raises_message_context_ok, emits_warning, emits_warning_on, eq_, eq_ignore_whitespace, eq_regex, expect_deprecated, expect_deprecated_20, expect_raises, expect_raises_message, expect_warnings, in_, is_, is_false, is_instance_of, is_none, is_not, is_not_, is_not_none, is_true, le_, ne_, not_in, not_in_, startswith_, uses_deprecated
from .config import async_test, combinations, combinations_list, db, fixture, requirements as requires
from .exclusions import _is_excluded, _server_version, against as _against, db_spec, exclude, fails, fails_if, fails_on, fails_on_everything_except, future, only_if, only_on, skip, skip_if
from .schema import eq_clause_element, eq_type_affinity
from .util import adict, fail, flag_combinations, force_drop_names, lambda_combinations, metadata_fixture, provide_metadata, resolve_lambda, rowset, run_as_contextmanager, teardown_events
from .warnings import assert_warnings, warn_test_suite

def against(*queries): # -> bool:
    ...

crashes = ...