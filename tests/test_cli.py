import contextlib
from unittest import mock
from argparse_plus import parser
import pytest


@pytest.fixture(scope="function")
def cli():
    from argparse import Namespace, ArgumentParser

    with contextlib.ExitStack() as stack:
        mcks = {}
        mcks["exit"] = stack.enter_context(mock.patch.object(ArgumentParser, "exit"))
        mcks["error"] = stack.enter_context(mock.patch.object(ArgumentParser, "error"))
        mcks["_print_message"] = stack.enter_context(
            mock.patch.object(ArgumentParser, "_print_message")
        )

        # fix for changes between 3.9 -> 3.10
        class MethodWrapper:
            def __init__(self, fn):
                self.fn = fn

            def __call__(self, instance, *args, **kwargs):
                from sys import version_info

                if (version_info < (3, 10)) and args == ("options",) and not kwargs:
                    args = ("positional arguments",)
                return self.fn(instance, *args, **kwargs)

        wrapper = MethodWrapper(ArgumentParser.add_argument_group)
        mcks["_add_argument_group"] = stack.enter_context(
            mock.patch.object(ArgumentParser, "add_argument_group", autospec=True)
        )
        mcks["_add_argument_group"].side_effect = wrapper
        yield Namespace(**mcks)


def test_cli_help(cli):
    "test the --help flag to the cli"
    p = parser.ArgumentParser(prog="abc.def", formatter_class="test")
    p.parse_args(["--help"])

    assert (
        cli._print_message.call_args[0][0].strip()
        == """
usage: abc.def [-h]

positional arguments:
  -h, --help  show this help message and exit
""".strip()
    )
