# pylint: disable=missing-module-docstring

from core import do_core_stuff


def test_core():
    assert do_core_stuff() == "wow"
