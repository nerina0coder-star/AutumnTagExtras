
from Autumn.exceptions import OptimizedError

from AutumnTagExtras.Content.abstract_content import AbstractContent


class Break(AbstractContent):
    """
    Represents a visual break in the document.
    """

    def __init__(self) -> None:
        self.name = "br"

        super().__init__()

    def __mul__(self, other) -> list["Break"]: # type: ignore
        if not isinstance(other, int):
            raise NotImplementedError("Only integers are allowed")
        if not type(self) == Break:
            raise OptimizedError("Break")
        return [Break() for _ in range(other)]