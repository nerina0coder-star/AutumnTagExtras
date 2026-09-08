from Autumn.Naming import Identifier

from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Typing import ContentChildren, Classes


class Abbreviation(AbstractContent):

    def __init__(self,
                 *content: ContentChildren,
                 description: str | None = None,
                 classes: Classes | None = None,
                 identifier: Identifier | None = None) -> None: ...
