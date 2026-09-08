from AutumnTagExtras.Content.abstract_content import AbstractContent
from AutumnTagExtras.Enums import FormRequestMethods
from AutumnTagExtras.Typing import ContentChildren


class Form(AbstractContent):

    def __init__(self,
                 *content: ContentChildren,
                 method: FormRequestMethods | None = None,
                 to: str | None = None) -> None: ...