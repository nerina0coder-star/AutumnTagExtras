from Autumn.Naming import Identifier

from AutumnTagExtras.Content.Text.heading import Heading
from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Typing import ContentChildren, Classes


class Section(AbstractContent):

    def __init__(self,
                 heading: Heading,
                 *content: ContentChildren,
                 identifier: Identifier | None = None,
                 classes: Classes | None = None) -> None: ...