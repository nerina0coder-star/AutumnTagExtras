from AutumnTagExtras.Content.abstract_content import AbstractContent


class Title(AbstractContent):
    """
    A tag used to mention a work's title. A work's title is NOT the author's name.
    """

    def __init__(self, *content,
                 classes = None,
                 identifier = None):
        self.tags = list(content)
        self.name = "cite"
        self.closable = True

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        super().__init__()