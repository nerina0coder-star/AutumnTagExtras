from Autumn.Naming import Class

from AutumnTagExtras.Content.abstract_content import AbstractContent

type ContentChildren = str | AbstractContent
type Classes = Class | list[Class]

class Typing:
    ContentChildren = ContentChildren
    Classes = Classes