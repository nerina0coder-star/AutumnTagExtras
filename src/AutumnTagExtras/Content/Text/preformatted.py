from AutumnTagExtras.Content.abstract_content import AbstractContent


class Preformatted(AbstractContent):
    """
    Indicates that the content(text) is already formatted.
    The line-breaks, spaces, and fonts are preserved and not changed by the browser.
    """

    def __init__(self,
                 *content,
                 classes = None,
                 identifier = None,):
        self.name = "pre"
        self.closable = True
        self.tags = list(content)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        super().__init__()