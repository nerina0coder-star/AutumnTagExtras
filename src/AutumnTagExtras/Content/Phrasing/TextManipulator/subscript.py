from AutumnTagExtras.Content.abstract_content import AbstractContent


class Subscript(AbstractContent):
    """
    Turns the content(text) into Subscript, can be used for creating chemical expressions, etc.
    """
    def __init__(self, *content):
        self.tags = list(content)
        self.name = "sub"
        self.closable = True

        super().__init__()