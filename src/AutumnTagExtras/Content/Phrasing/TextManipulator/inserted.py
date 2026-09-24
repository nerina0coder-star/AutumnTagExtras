from AutumnTagExtras.Content.abstract_content import AbstractContent


class Inserted(AbstractContent):
    """
    Indicates the content(text) of this tag has been inserted into the document.
    """
    def __init__(self, *content):
        self.tags = list(content)
        self.name = "ins"
        self.closable = True

        super().__init__()