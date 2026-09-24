from AutumnTagExtras.Content.abstract_content import AbstractContent


class Section(AbstractContent):
    """
    Represents a section of the document, used to separate different parts of
    the document.

    In real world, you must use this tag to separate different sections of the
    document, NOT for simple styling.

    For styling, the tag used is Division.
    """

    def __init__(self,
                 heading,
                 *content,
                 identifier = None,
                 classes = None):
        self.name = "section"

        if identifier:
            self.identifier = identifier

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        self.closable = True
        self.tags = [heading, *content]

        super().__init__()

