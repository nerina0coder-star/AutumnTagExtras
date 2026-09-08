from typing import ClassVar

from .body import Body
from .division import Division
from .footer import Footer
from .form import Form
from .header import Header
from .main import Main
from .navbar import Navbar
from .section import Section

class Containers:

    Body: ClassVar[type[Body]]
    Division: ClassVar[type[Division]]
    Section: ClassVar[type[Section]]
    Main: ClassVar[type[Main]]
    Header: ClassVar[type[Header]]
    Navbar: ClassVar[type[Navbar]]
    Form: ClassVar[type[Form]]
    Footer: ClassVar[type[Footer]]
