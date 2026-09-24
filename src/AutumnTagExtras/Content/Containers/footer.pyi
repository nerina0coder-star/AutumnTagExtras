from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Typing import ContentChildren, Classes


class Footer(AbstractContent):

    def __init__(self,
                 *content: ContentChildren,
                 classes: Classes | None = None) -> None: ...