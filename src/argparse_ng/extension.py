class ExtentionError(Exception):
    pass


class DuplicateExtensionNameError(ExtentionError):
    pass


class MissingExtensionNameError(ExtentionError):
    pass


class ExtensionBase:
    NAME = (
        None  # an extension can define a unique name or have it defined by the __name__
    )

    @classmethod
    def get(cls, name):
        classes = {}

        def walks(node):
            for subclass in node.__subclasses__():
                sname = subclass.NAME or subclass.__name__
                if sname.lower() in classes:
                    raise DuplicateExtensionNameError(
                        f"duplicate subclass with name='{sname}' found",
                        sname,
                        subclass,
                        classes[sname.lower()],
                    )
                classes[sname] = subclass
                if subclass.__subclasses__():
                    walks(subclass)

        walks(cls)
        key = name.replace("-", "_").lower()
        if key.lower().endswith("extension"):
            key = key[: -len("extension")]
        if key not in classes:
            raise MissingExtensionNameError(
                f"cannot find extension {name}", name, key, list(classes)
            )

    def __init__(self, name):
        self.name = name

    def setup(self, fn, arguments):
        return fn

    def process(self, kwargs, arguments):
        pass
