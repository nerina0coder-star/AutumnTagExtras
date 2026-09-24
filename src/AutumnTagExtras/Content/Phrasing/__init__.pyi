from typing import ClassVar

from .TextManipulator import TextManipulator
from .Reference import Reference
from .anchor import Anchor
from .break_ import Break
from .directional_override import DirectionalOverride
from .phrase import Phrase

class Phrasing:

    Anchor: ClassVar[type[Anchor]]
    Break: ClassVar[type[Break]]
    DirectionalOverride: ClassVar[type[DirectionalOverride]]
    Phrase: ClassVar[type[Phrase]]
    Reference: ClassVar[type[Reference]]
    TextManipulator: ClassVar[type[TextManipulator]]