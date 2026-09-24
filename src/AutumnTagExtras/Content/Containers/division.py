from AutumnTagExtras.Content.abstract_content import AbstractContent


class Division(AbstractContent):
    """
    Division - Used to divide each part of the layout without any additional semantical meaning.
    """

    def __init__(self,
                 *content,
                 classes = None,
                 identifier = None):
        self.name = "div"
        self.closable = True

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        self.tags = list(content)

        super().__init__()