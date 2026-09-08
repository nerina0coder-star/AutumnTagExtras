from AutumnTagExtras.Content.abstract_content import AbstractContent


class Main(AbstractContent):
    """
    Main contains the main content of out document.
    """

    def __init__(self,
                 *content,
                 classes = None):
        self.name = "main"
        self.closable = True
        self.content = list(content)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        super().__init__()