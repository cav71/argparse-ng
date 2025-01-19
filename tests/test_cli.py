import contextlib
import sys
from unittest import mock

import pytest
from argparse_plus import parser


@pytest.fixture(scope="function")
def cli():
    from argparse import ArgumentParser, Namespace

    with contextlib.ExitStack() as stack:
        mcks = {}
        mcks["exit"] = stack.enter_context(mock.patch.object(ArgumentParser, "exit"))
        mcks["error"] = stack.enter_context(mock.patch.object(ArgumentParser, "error"))
        mcks["_print_message"] = stack.enter_context(
            mock.patch.object(ArgumentParser, "_print_message")
        )
        yield Namespace(**mcks)


def test_cli_help(cli):
    "test the --help flag to the cli"
    p = parser.ArgumentParser(prog="abc.def", formatter_class="test")
    p.parse_args(["--help"])

    txt = cli._print_message.call_args[0][0].strip()
    if sys.version_info < (3, 10):
        txt = txt.replace("\npositional arguments:\n", "\noptions:\n")
        txt = txt.replace("\noptional arguments:\n", "\noptions:\n")
    assert (
        txt
        == """
usage: abc.def [-h]

options:
  -h, --help  show this help message and exit
""".strip()
    )
