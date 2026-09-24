from AutumnTagExtras.Content.abstract_content import AbstractContent


class DirectionalOverride(AbstractContent):
    """
    Changes the direction of the content.
    """

    def __init__(self,
                 *content,
                 classes = None,
                 identifier = None):
        self.tags = list(content)
        self.name = "bdo"
        self.closable = True

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        super().__init__()
