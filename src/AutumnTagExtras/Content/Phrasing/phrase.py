from AutumnTagExtras.Content.abstract_content import AbstractContent


class Phrase(AbstractContent):
    """
    Phrases work the same as paragraphs, but with the difference that Phrases take space
    for their content, while paragraphs take as much as possible.
    """

    def __init__(self,
                 *content,
                 classes = None,
                 identifier = None):
        self.name = "span"
        self.tags = list(content)
        self.closable = True

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        super().__init__()