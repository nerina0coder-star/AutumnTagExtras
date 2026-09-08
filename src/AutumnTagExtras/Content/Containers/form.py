from AutumnTagExtras.Content.abstract_content import AbstractContent


class Form(AbstractContent):
    """
    Represents a form with input fields.
    """

    def __init__(self,
                 *content,
                 method = None,
                 to: str = None,
                 classes = None,
                 identifier = None):
        """
        To: The URL to send the request to.
        """

        self.name = "form"
        self.closable = True
        self.tags = list(content)

        if method:
            self.attributes.setdefault("method", method)

        if to:
            self.attributes.setdefault("action", to)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        super().__init__()
