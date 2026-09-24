from AutumnTagExtras.Content.abstract_content import AbstractContent


class Small(AbstractContent):
    """
    Represents a side-comment by making the content(text) smaller.
    """
    def __init__(self, *content):
        self.tags = list(content)
        self.name = "small"
        self.closable = True

        super().__init__()