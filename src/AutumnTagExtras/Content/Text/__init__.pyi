from typing import ClassVar

from .address import Address
from .heading import Heading
from .paragraph import Paragraph
from .preformatted import Preformatted
from .quote import Quote

class Text:
    Address: ClassVar[type[Address]]
    Heading: ClassVar[type[Heading]]
    Paragraph: ClassVar[type[Paragraph]]
    Preformatted: ClassVar[type[Preformatted]]
    Quote: ClassVar[type[Quote]]
