from AutumnTagExtras.Content.abstract_content import AbstractContent


class Strong(AbstractContent):
    """
    Increases the impact of the content(text), often used
    to indicate that the content is important.
    """

    def __init__(self, *content):
        self.tags = list(content)
        self.name = "strong"
        self.closable = True
        super().__init__()
