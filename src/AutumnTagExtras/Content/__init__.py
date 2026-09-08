from .Text import Text
from .Phrasing import Phrasing
from .Containers import Containers
from .horizontal_break import HorizontalBreak
from .abstract_content import AbstractContent

class Content:
    """
    This package contains classes/tags that are meant to be visible in the document(DOM)
    """

    Text = Text
    Phrasing = Phrasing
    Containers = Containers
    HorizontalBreak = HorizontalBreak

    BaseContent = AbstractContent
