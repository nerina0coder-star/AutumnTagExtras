
from Autumn.exceptions import OptimizedError

from AutumnTagExtras.Content.abstract_content import AbstractContent


class Bold(AbstractContent):
    """
    A tag used to make a text bold. To increase the text's impact, Strong(<strong>) is used.
    """
    def __init__(self, *content):
        self.closable = True
        self.tags = list(content)
        self.name = "b"

        super().__init__()

    def __mul__(self, other: int):
        if not isinstance(other, int):
            raise NotImplementedError()
        if not type(self) == Bold:
            raise OptimizedError("Bold")

        return [Bold(*self.tags) for _ in range(other)]