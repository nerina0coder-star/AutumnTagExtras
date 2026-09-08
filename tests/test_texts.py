import unittest

from Autumn import new

from AutumnTagExtras import Branch


class Test(unittest.TestCase):
    def setUp(self):
        base = new()

        with base:
            self.branch = Branch()

    def test_address(self):
        address = self.branch.content.Text.Address()

        self.assertEqual(address.build(), "<address></address>")

    def test_heading(self):
        heading = self.branch.content.Text.Heading(self.branch.e.Headings.TITLE)

        self.assertEqual(heading.build(), "<h1></h1>")

    def test_paragraph(self):
        paragraph = self.branch.content.Text.Paragraph()

        self.assertEqual(paragraph.build(), "<p></p>")

    def test_preformatted(self):
        preformatted = self.branch.content.Text.Preformatted()

        self.assertEqual(preformatted.build(), "<pre></pre>")

    def test_quote(self):
        quote = self.branch.content.Text.Quote()

        self.assertEqual(quote.build(), "<blockquote></blockquote>")
