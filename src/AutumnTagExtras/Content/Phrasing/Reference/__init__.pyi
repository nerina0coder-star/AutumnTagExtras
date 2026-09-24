from typing import ClassVar

from .quote import Quote
from .abbreviation import Abbreviation
from .title import Title

class Reference:

    Quote: ClassVar[type[Quote]]
    Abbreviation: ClassVar[type[Abbreviation]]
    Title: ClassVar[type[Title]]