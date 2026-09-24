from AutumnTagExtras.Content.abstract_content import AbstractContent


class Navbar(AbstractContent):
    """
    Navbar contains the links used for navigation.
    """

    def __init__(self,
                 *content,
                 classes = None):
        self.name = "nav"
        self.closable = True
        self.contents = list(content)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        super().__init__()