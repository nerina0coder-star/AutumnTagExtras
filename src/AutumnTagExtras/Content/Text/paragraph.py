from AutumnTagExtras.Content.abstract_content import AbstractContent


class Paragraph(AbstractContent):
    """
    A simple Paragraph in the document. Be aware that paragraphs are block.
    (They take the whole horizontal space, as much as possible).
    """
    def __init__(self,
                 *content,
                 classes = None,
                 identifier = None):
        self.name = "p"
        self.closable = True
        self.tags = list(content)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        super().__init__()