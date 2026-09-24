from collections.abc import Callable
from functools import wraps
from inspect import isroutine, signature
from typing import Any

from Autumn.Tag.abstract_tag import AbstractTag


class DeclarativeTag(AbstractTag):
    __no_new__ = True

    def __init_subclass__(cls, **_kwargs: Any) -> None:
        if "__init__" in cls.__dict__:
            super().__init_subclass__(**_kwargs)
            return

        properties = {}
        attributes_dynamic = False

        for i in ["name", "closable", "dynamic",
                  "preferred_parent", "identifier",
                  "classes", "worth"]:
            if i in cls.__dict__:
                properties[i] = getattr(cls, i)
                if hasattr(properties[i], "copy") and len(signature(properties[i].copy).parameters) == 1 \
                        and list(signature(properties[i].copy).parameters.keys())[0] == "self":
                    properties[i] = properties[i].copy()

        for i in cls.__dict__.keys():
            if i.startswith("attr_"):
                name = i[len("attr_"):].replace("_", "-")
                properties.setdefault("attributes", {})[name] = getattr(cls, i)
                if isroutine(properties["attributes"][name]):
                    attributes_dynamic = True

        if "content" in cls.__dict__:
            properties["tags"] = getattr(cls, "content")

            if not isinstance(properties["tags"], (list, Callable)): # type: ignore[arg-type]
                if not isinstance(properties["tags"], (str, AbstractTag, Callable)): # type: ignore[arg-type]
                    raise ValueError("Content can only contain AbstractTags and strings.")
                properties["tags"] = [properties["tags"]]

            if isinstance(properties["tags"], list):
                if len(properties["tags"]) > 0:
                    properties["closable"] = True

        if isroutine(properties.get("dynamic", None)):
            raise ValueError("Dynamic can't be callable.")

        if any(isroutine(prop) for prop in properties.values()):
            properties["dynamic"] = True

        if "preferred_parent" in properties:
            if not isroutine(properties["preferred_parent"]):
                current = properties["preferred_parent"]
                properties["preferred_parent"] = lambda self, *args, **kws: current

        static = dict(filter(lambda x: not isroutine(x[1]) and x[0] != "attributes", properties.items()))
        dynamic = dict(filter(lambda x: isroutine(x[1]) and x[0] != "attributes", properties.items()))

        original_init = cls.__init__
        original_before_build = cls.before_build

        @wraps(original_init)
        def init(self: DeclarativeTag, *args: Any, **kws: Any) -> None:
            for name, value in static.items():

                setattr(self, name, value)

            attributes: dict[str, Any] = {}

            for attr_name, attr_val in properties.get("attributes", {}).items():

                if isroutine(attr_val):
                    continue

                attributes[attr_name] = attr_val

            setattr(self, "attributes", attributes)

            original_init(self, *args, **kws)  # type: ignore[unused-ignore]

        @wraps(original_before_build)
        def before_build(self: DeclarativeTag, *args: Any, **kws: Any) -> None:
            for name, value in dynamic.items():
                if name != "tags":
                    setattr(self, name, value(self, **kws))
                    continue

                returned = value(self, self.tags, **kws)
                if returned:
                    setattr(self, name, returned)

            if attributes_dynamic:
                attributes: dict[str, Any] = {}
                for attr_name, attr_val in properties.get("attributes", {}).items():
                    if not isroutine(attr_val):
                        continue
                    attributes[attr_name] = attr_val(self, **kws)
                self.attributes.update(attributes)

            return original_before_build(self, *args, **kws)  #type: ignore[return-value]

        setattr(cls, "__init__", init)
        setattr(cls, "before_build", before_build)

    def __init__(self) -> None:
        self.content: list[AbstractTag | str] = []
        super().__init__()

