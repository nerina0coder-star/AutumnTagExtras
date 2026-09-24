from Autumn.Naming import Identifier

from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Enums import LinkTargets
from AutumnTagExtras.Typing import ContentChildren, Classes


class Anchor(AbstractContent):

    def __init__(self, url: str, *content: ContentChildren,
                 classes: Classes | None = None,
                 identifier: Identifier | None = None,
                 target: LinkTargets | None = None) -> None: ...

    @staticmethod
    def mail(address: str, *content: ContentChildren,
             classes: Classes | None = None,
             identifier: Identifier | None = None,
             target: LinkTargets | None = None) -> Anchor: ...