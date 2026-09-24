from AutumnTagExtras.Content.abstract_content import AbstractContent


class Deleted(AbstractContent):
    """
    Indicates that the content(text) has been deleted from the document.
    The browser usually strikes a line through the deleted text.
    """

    def __init__(self, *content):
        self.tags = list(content)
        self.name = "del"
        self.closable = True

        super().__init__()