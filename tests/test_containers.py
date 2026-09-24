import unittest

from Autumn import new

from AutumnTagExtras import Branch


class Test(unittest.TestCase):

    def setUp(self):
        base = new()

        with base:
            self.branch = Branch()

    def test_body(self):
        body = self.branch.content.Containers.Body()

        self.assertEqual(body.build(), "<body></body>")

    def test_division(self):
        div = self.branch.content.Containers.Division()

        self.assertEqual(div.build(), "<div></div>")

    def test_footer(self):
        footer = self.branch.content.Containers.Footer()

        self.assertEqual(footer.build(), "<footer></footer>")

    def test_form(self):
        form = self.branch.content.Containers.Form()

        self.assertEqual(form.build(), "<form></form>")

    def test_header(self):
        header = self.branch.content.Containers.Header()

        self.assertEqual(header.build(), "<header></header>")

    def test_main(self):
        main = self.branch.content.Containers.Main()

        self.assertEqual(main.build(), "<main></main>")

    def test_navbar(self):
        navbar = self.branch.content.Containers.Navbar()

        self.assertEqual(navbar.build(), "<nav></nav>")

    def test_section(self):
        section = self.branch.content.Containers.Section("")  # type: Ignore
        # The usage above is wrong, but we use this for testing only.

        self.assertEqual(section.build(), "<section></section>")
