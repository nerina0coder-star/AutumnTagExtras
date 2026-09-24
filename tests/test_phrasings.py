import unittest

from Autumn import new

from AutumnTagExtras import Branch


class Test(unittest.TestCase):

    def setUp(self):
        self.base = new()

        with self.base:
            self.branch = Branch()

    def test_break(self):
        br = self.branch.content.Phrasing.Break()

        mul = br * 10

        self.assertEqual(br.build(), "<br>")
        self.assertMultiLineEqual(self.branch.div(*mul).build(),
                                  "<div>" +
                                  "<br>" * 10 +
                                  "</div>")

    def test_anchor(self):
        a1 = self.branch.content.Phrasing.Anchor.mail("test@gmail.com",
                                                      "test")
        a2 = self.branch.content.Phrasing.Anchor("https://www.google.com",
                                                 "test")

        self.assertEqual(a1.build(),
                         '<a href="mailto:test@gmail.com">test</a>')
        self.assertEqual(a2.build(),
                         '<a href="https://www.google.com">test</a>')

    def test_directional_override(self):
        bdo = self.branch.content.Phrasing.DirectionalOverride("abc")
        self.assertEqual(bdo.build(),
                         "<bdo>abc</bdo>")

    def test_phrase(self):
        phrase = self.branch.content.Phrasing.Phrase("abc")
        self.assertEqual(phrase.build(),
                         "<span>abc</span>")

class TestReference(unittest.TestCase):
    def setUp(self):
        self.base = new()
        with self.base:
            self.branch = Branch()

    def test_abbreviation(self):
        abbr = self.branch.content.Phrasing.Reference.Abbreviation("abc",
                                                                   description="module abc of python")
        self.assertEqual(abbr.build(),
                         '<abbr title="module abc of python">abc</abbr>')

    def test_quote(self):
        q = self.branch.content.Phrasing.Reference.Quote("I wear no mask",
                                                         source="https://thekinginyellow.test.com")

        self.assertEqual(q.build(),
                         '<q cite="https://thekinginyellow.test.com">I wear no mask</q>')

    def test_title(self):
        title = self.branch.content.Phrasing.Reference.Title("The King In Yellow")

        self.assertEqual(title.build(),
                         "<cite>The King In Yellow</cite>")


class TestTextManipulator(unittest.TestCase):

    def setUp(self):
        self.base = new()

        with self.base:
            self.branch = Branch()

    def test_bold(self):
        bold = self.branch.content.Phrasing.TextManipulator.Bold("abc")

        self.assertEqual(bold.build(),
                         "<b>abc</b>")

    def test_deleted(self):
        deleted = self.branch.content.Phrasing.TextManipulator.Deleted("abc")

        self.assertEqual(deleted.build(),
                         "<del>abc</del>")

    def test_emphasized(self):
        em = self.branch.content.Phrasing.TextManipulator.Emphasized("abc")

        self.assertEqual(em.build(),
                         "<em>abc</em>")

    def test_inserted(self):
        ins = self.branch.content.Phrasing.TextManipulator.Inserted("abc")

        self.assertEqual(ins.build(),
                         "<ins>abc</ins>")

    def test_italic(self):
        italic = self.branch.content.Phrasing.TextManipulator.Italic("abc")

        self.assertEqual(italic.build(),
                         "<i>abc</i>")

    def test_mark(self):
        mark = self.branch.content.Phrasing.TextManipulator.Mark("abc")

        self.assertEqual(mark.build(),
                         "<mark>abc</mark>")

    def test_small(self):
        small = self.branch.content.Phrasing.TextManipulator.Small("abc")

        self.assertEqual(small.build(),
                         "<small>abc</small>")

    def test_strong(self):
        strong = self.branch.content.Phrasing.TextManipulator.Strong("abc")

        self.assertEqual(strong.build(),
                         "<strong>abc</strong>")

    def test_subscript(self):
        sub = self.branch.content.Phrasing.TextManipulator.Subscript("abc")

        self.assertEqual(sub.build(),
                         "<sub>abc</sub>")

    def test_superscript(self):
        sup = self.branch.content.Phrasing.TextManipulator.Superscript("abc")

        self.assertEqual(sup.build(),
                         "<sup>abc</sup>")
