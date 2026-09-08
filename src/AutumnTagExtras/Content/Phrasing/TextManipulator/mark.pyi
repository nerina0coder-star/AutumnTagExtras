from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Typing import ContentChildren


class Mark(AbstractContent):

    def __init__(self,
                 *content: ContentChildren): ...