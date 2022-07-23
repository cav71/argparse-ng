import contextlib
from unittest import mock
from argparse_plus import parser
import pytest

@pytest.fixture(scope="function")
def cli():
    from argparse import Namespace, ArgumentParser
    with contextlib.ExitStack() as stack:
        mcks = {}
        mcks["exit"] = stack.enter_context(
            mock.patch.object(ArgumentParser, "exit")
        )
        mcks["error"] = stack.enter_context(
            mock.patch.object(ArgumentParser, "error")
        )
        mcks["_print_message"] = stack.enter_context(
            mock.patch.object(ArgumentParser, "_print_message")
        )
        yield Namespace(**mcks)


def test_cli_help(cli):
    "test the --help flag to the cli"
    p = parser.ArgumentParser(prog="abc.def", formatter_class="test")
    p.parse_args(["--help"])

    def s(txt):
        "handles all the --help output weirdnesses"
        if ".py optional arguments:" in txt:
            result = txt.replace(".py optional arguments:", ".py options:")
        return result
    assert cli._print_message.call_args[0][0].strip() == """
usage: abc.def [-h]

optional arguments:
  -h, --help  show this help message and exit
""".strip()

