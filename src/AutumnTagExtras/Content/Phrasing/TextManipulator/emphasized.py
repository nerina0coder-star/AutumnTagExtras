from AutumnTagExtras.Content.abstract_content import AbstractContent


class Emphasized(AbstractContent):
    """
    Indicates the content is emphasized.
    """

    def __init__(self, *content):
        self.tags = list(content)
        self.name = "em"
        self.closable = True

        super().__init__()