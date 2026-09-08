from Autumn.Naming import Identifier

from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Typing import ContentChildren, Classes


class Division(AbstractContent):

    def __init__(self,
                 *content: ContentChildren,
                 classes: Classes | None = None,
                 identifier: Identifier | None = None) -> None: ...