from __future__ import annotations

import argparse
from typing import Sequence, Optional, Tuple, Dict, Any

from . import tools

def get_formatter_class(formatter=None):
    from argparse import ArgumentDefaultsHelpFormatter, RawDescriptionHelpFormatter, RawTextHelpFormatter
    if formatter == "test":
        formatter = RawTextHelpFormatter
    elif not formatter:
        class Formatter(ArgumentDefaultsHelpFormatter, RawTextHelpFormatter):
            pass
        formatter = Formatter
    return formatter


class ArgumentParser(argparse.ArgumentParser):
    class NotAssigned:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f"<{self.__class__.__name__} value={self.value} at {hex(id(self))}>"

    def __init__(self, *args: Any, **kwargs):
        kwargs["formatter_class"] = get_formatter_class(kwargs.get("formatter_class"))
        super().__init__(*args, **kwargs)
        self.argument_default = ArgumentParser.NotAssigned(ArgumentParser.NotAssigned)

    def parse_known_args(
        self, args: Optional[Sequence[str]]=None, namespace: Optional[argparse.Namespace] = None
    ) -> tuple[argparse.Namespace, list[str]]:

        return super().parse_known_args(args, namespace)
