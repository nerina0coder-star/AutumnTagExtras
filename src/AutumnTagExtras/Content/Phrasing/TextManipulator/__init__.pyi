from typing import ClassVar

from .small import Small
from .mark import Mark

from .emphasized import Emphasized
from .italic import Italic

from .bold import Bold
from .strong import Strong

from .inserted import Inserted
from .deleted import Deleted

from .subscript import Subscript
from .superscript import Superscript

class TextManipulator:

    Small: ClassVar[type[Small]]
    Mark: ClassVar[type[Mark]]

    Emphasized: ClassVar[type[Emphasized]]
    Italic: ClassVar[type[Italic]]

    Bold: ClassVar[type[Bold]]
    Strong: ClassVar[type[Strong]]

    Inserted: ClassVar[type[Inserted]]
    Deleted: ClassVar[type[Deleted]]

    Subscript: ClassVar[type[Subscript]]
    Superscript: ClassVar[type[Superscript]]
