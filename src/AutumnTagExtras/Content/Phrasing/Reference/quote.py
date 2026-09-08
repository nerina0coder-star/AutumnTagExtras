from AutumnTagExtras.Content.abstract_content import AbstractContent


class Quote(AbstractContent):
    """
    Used to quote a single/short line from another source without breaking the
    flow/line, used inside other tags that can contain text.
    """

    def __init__(self, *content,
                 source = None,
                 classes = None,
                 identifier = None):
        self.name = "q"
        self.tags = list(content)
        self.closable = True
        if source:
            self.attributes = {
                "cite": source
            }

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        super().__init__()