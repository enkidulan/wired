import os
import sys

import pytest

if sys.version_info < (3, 7):  # pragma: no cover
    collect_ignore_glob = ['*.py']


@pytest.fixture(scope="session", autouse=True)
def examples_path():
    tutorial_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../docs/tutorial/sample_framework_with_addons')
    )
    sys.path.insert(0, tutorial_path)
