from typing import ClassVar

from .Text import Text
from .Phrasing import Phrasing
from .Containers import Containers
from .horizontal_break import HorizontalBreak
from .abstract_content import AbstractContent

class Content:

    Text: ClassVar[type[Text]]
    Phrasing: ClassVar[type[Phrasing]]
    Containers: ClassVar[type[Containers]]
    HorizontalBreak: ClassVar[type[HorizontalBreak]]

    BaseContent: ClassVar[type[AbstractContent]]