"""
Autumn Tag Extras
The project containing extra tags that can be used with Autumn.
"""
from Autumn.base import current_base

from Autumn import Base as AutumnBase
from .autumn import Base

with Base:
    from .Typing import Typing
    from .Content import Content
    from .Enums import Enums


class Branch:
    """
    The tag branch of autumn.
    """

    def __init__(self) -> None:
        base = current_base.this()

        AutumnBase.merge(base, Base)

        self._base = base
        self.e = Enums
        self.typing = Typing
        self.content = Content

        self.p = self.content.Text.Paragraph
        self.div = self.content.Containers.Division
        self.form = self.content.Containers.Form

        base.extensions = self

        base.tag.alias("p", self.p)
        base.tag.alias("div", self.div)
        base.tag.alias("form", self.form)

__all__ = ["Branch"]
