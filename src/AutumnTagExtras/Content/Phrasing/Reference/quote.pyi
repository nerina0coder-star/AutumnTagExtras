from Autumn.Naming import Identifier

from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Typing import ContentChildren, Classes


class Quote(AbstractContent):

    def __init__(self,
                 *content: ContentChildren,
                 source: str | None = None,
                 classes: Classes | None = None,
                 identifier: Identifier | None = None) -> None: ...