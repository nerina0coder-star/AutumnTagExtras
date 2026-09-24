from AutumnTagExtras.Content.abstract_content import AbstractContent


class HorizontalBreak(AbstractContent):
    """
    The only thematically used tag, creates a horizontal break.
    """

    def __init__(self) -> None:
        self.name = "hr"

        super().__init__()