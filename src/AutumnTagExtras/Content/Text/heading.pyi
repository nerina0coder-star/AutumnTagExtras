from Autumn.Naming import Identifier

from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Enums import Headings
from AutumnTagExtras.Typing import ContentChildren, Classes


class Heading(AbstractContent):

    def __init__(self,
                 heading: Headings,
                 *content: ContentChildren,
                 identifier: Identifier | None = None,
                 classes: Classes | None = None) -> None: ...