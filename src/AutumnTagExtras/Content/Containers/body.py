from AutumnTagExtras.Content.abstract_tagbase import AbstractTagBase


class Body(AbstractTagBase): # Since it must not be used in other tags, it won't inherit from AbstractContent.
    """
    Body - The class used to hold all visible(to the eye) tags.
    All tags in this tag MUST be visible to the eye in the document.
    """

    def __init__(self,
                 *content,
                 classes = None):
        self.name = "body"
        self.closable = True

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]

        self.content = list(content)

        super().__init__()