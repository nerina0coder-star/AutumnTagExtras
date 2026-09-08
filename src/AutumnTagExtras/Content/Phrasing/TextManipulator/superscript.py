from AutumnTagExtras.Content.abstract_content import AbstractContent


class Superscript(AbstractContent):
    """
    Turns the content(text) into Superscript, can be used for creating footnotes, etc.
    """
    def __init__(self, *content):
        self.tags = list(content)
        self.name = "sup"
        self.closable = True

        super().__init__()