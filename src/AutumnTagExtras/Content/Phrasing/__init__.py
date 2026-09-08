from .TextManipulator import TextManipulator
from .Reference import Reference
from .anchor import Anchor
from .break_ import Break
from .directional_override import DirectionalOverride
from .phrase import Phrase

class Phrasing:
    """
    Phrasing - The package containing the tags used for semantic AND phrasing purposes.
    The tags of this package should not be misused, as they serve semantic meanings ONLY.
    """
    Anchor = Anchor
    Break = Break
    DirectionalOverride = DirectionalOverride
    Phrase = Phrase
    TextManipulator = TextManipulator
    Reference = Reference