from AutumnTagExtras.Content.abstract_content import AbstractContent


class Italic(AbstractContent):
    """
    Makes the content(text) italic.
    """
    def __init__(self, *content):
        self.tags = list(content)
        self.name = "i"
        self.closable = True

        super().__init__()