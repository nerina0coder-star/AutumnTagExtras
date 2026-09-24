from AutumnTagExtras.Content.abstract_content import AbstractContent


class Anchor(AbstractContent):
    """
    Represents a clickable/activatable link to the same website or another website.
    """

    def __init__(self, url, *children,
                 classes = None,
                 identifier = None,
                 target = None):
        self.name = "a"
        self.closable = True
        self.attributes = {
            "href": url,
        }
        self.tags = list(children)

        if classes:
            self.classes = classes if isinstance(classes, list) else [classes]
        if identifier:
            self.identifier = identifier
        if target:
            self.attributes.setdefault("target", str(target))

        super().__init__()

    @staticmethod
    def mail(address, *children,
             classes = None,
             identifier = None,
             target = None):
        """
        Creates a link to an email address.
        """

        return Anchor(f"mailto:{address}", *children,
                      classes=classes, identifier=identifier, target=target)