from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Typing import ContentChildren


class Bold(AbstractContent):

    def __init__(self, *content: ContentChildren) -> None: ...

    def __mul__(self, other: int) -> list["Bold"]: ... # type: ignore