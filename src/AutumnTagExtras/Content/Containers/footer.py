from AutumnTagExtras.Content.abstract_content import AbstractContent


class Footer(AbstractContent):
    """
    A footer in our document.
    """

    def __init__(self,
                 *content,
                 classes = None):
        self.name = "footer"
        self.closable = True

        self.tags = list(content)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        super().__init__()