from AutumnTagExtras.Content.abstract_content import AbstractContent


class Address(AbstractContent):
    """
    Represents the contact information of the author/owner of the document or article.
    """

    def __init__(self,
                 *content,
                 classes = None):
        self.name = "address"
        self.closable = True
        self.tags = list(content)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        super().__init__()