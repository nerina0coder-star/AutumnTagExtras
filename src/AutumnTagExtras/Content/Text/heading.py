from AutumnTagExtras.Content.abstract_content import AbstractContent


class Heading(AbstractContent):

    def __init__(self,
                 heading,
                 *content,
                 identifier = None,
                 classes = None):

        self.name = heading.value
        self.closable = True
        self.tags = list(content)

        if identifier:
            self.identifier = identifier
        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        super().__init__()
