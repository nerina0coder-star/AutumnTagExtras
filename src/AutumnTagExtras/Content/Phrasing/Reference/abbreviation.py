from AutumnTagExtras.Content.abstract_content import AbstractContent


class Abbreviation(AbstractContent):
    """
    Indicates the content is an abbreviation or an acronym,
    e.g., CSP(Stands for Content Security Policy).
    """

    def __init__(self,
                 *content,
                 description = None,
                 classes = None,
                 identifier = None):
        self.tags = list(content)
        self.name = "abbr"
        self.closable = True

        if description:
            self.attributes = {
                "title": description,
            }

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        if identifier:
            self.identifier = identifier

        super().__init__()