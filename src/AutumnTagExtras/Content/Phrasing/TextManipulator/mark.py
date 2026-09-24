from AutumnTagExtras.Content.abstract_content import AbstractContent


class Mark(AbstractContent):
    """
    Defines the content(text) to be highlighted.
    """
    def __init__(self, *content):
        self.tags = list(content)
        self.closable = True
        self.name = "mark"

        super().__init__()