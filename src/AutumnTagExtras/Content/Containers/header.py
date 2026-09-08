from AutumnTagExtras.Content.abstract_content import AbstractContent


class Header(AbstractContent):
    """
    Header is the header of our document.
    """

    def __init__(self,
                 *content,
                 classes = None):
        self.name = "header"
        self.closable = True
        self.tags = list(content)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        super().__init__()