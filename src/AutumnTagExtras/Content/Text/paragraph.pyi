from Autumn.Naming import Identifier

from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Typing import ContentChildren, Classes


class Paragraph(AbstractContent):

    def __init__(self,
                 *content: ContentChildren,
                 identifier: Identifier | None = None,
                 classes: Classes | None = None) -> None: ...