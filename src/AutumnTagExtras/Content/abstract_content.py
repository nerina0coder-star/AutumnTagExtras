from AutumnTagExtras.Content.abstract_tagbase import AbstractTagBase

class AbstractContent(AbstractTagBase):
    """
    The base class that means the subclass IS a content, therefore visible to the eye.
    """

    __no_new__ = True