from AutumnTagExtras.Content.abstract_content import AbstractContent


class Quote(AbstractContent):
    """
    Used to quote multiple lines of text from another source.
    The browser usually adds indention to this tag's right and left to make it stand out.
    """

    def __init__(self,
                 *content,
                 classes = None,
                 identifier = None,):
        self.name = "blockquote"
        self.closable = True
        self.tags = list(content)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        super().__init__()