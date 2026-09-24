from Autumn.Tag import AbstractTag

from AutumnTagExtras.Typing import ContentChildren, Classes


class Body(AbstractTag):

    def __init__(self,
                 *content: ContentChildren,
                 classes: Classes | None = None) -> None: ...