import unittest
from typing import Any

from Autumn import new
from Autumn.base import current_base

from AutumnTagExtras import Branch


class Test(unittest.TestCase):

    def setUp(self) -> None:
        with new():
            self.Base = current_base.this()
            self.branch = Branch()

    def test_static_only(self) -> None:

        class StaticTag(self.branch.DeclarativeTag):
            name = "test"
            closable = True

        class StaticTag2(self.branch.DeclarativeTag):
            name = "test"
            content = "abc"

        class StaticTag3(self.branch.DeclarativeTag):
            name = "test"
            attr_testing = True

        for i in range(10):
            tag1 = StaticTag()
            tag2 = StaticTag2()

            self.assertEqual(tag1.name, "test")
            self.assertEqual(tag2.name, "test")
            self.assertEqual(tag2.tags, ["abc"])
            self.assertTrue(tag1.closable)
            self.assertTrue(tag2.closable)
            self.assertFalse(tag1.dynamic)
            self.assertFalse(tag2.dynamic)

            self.assertEqual(StaticTag().build(), "<test></test>")
            self.assertEqual(StaticTag2().build(), "<test>abc</test>")
            self.assertEqual(StaticTag3().build(), "<test testing>")

    def test_dynamic_only(self) -> None:
        class DynamicTag(self.branch.DeclarativeTag):
            closable = True

            def name(self, **kwargs) -> str | Any:
                if "name" in kwargs:
                    return kwargs["name"]
                return "div"

        class DynamicTag2(self.branch.DeclarativeTag):
            closable = True

            def name(self, **kwargs) -> str:
                if "name" in kwargs:
                    name: str = kwargs["name"]
                    return name
                return "div"

            def content(self, content: list, /, **kwargs):
                if "add" in kwargs:
                    content.append(kwargs["add"])

        class DynamicTag3(self.branch.DeclarativeTag):

            closable = True

            def name(self, **kwargs):
                if "name" in kwargs:
                    return kwargs["name"]
                return "div"

            def attr_testing(self, **kwargs):
                if "testing" in kwargs:
                    return kwargs["testing"]
                return True

        for _ in range(10):
            self.assertTrue(DynamicTag().dynamic)
            self.assertTrue(DynamicTag2().dynamic)
            self.assertTrue(DynamicTag3().dynamic)

            self.assertEqual(DynamicTag().build(), "<div></div>")
            self.assertEqual(DynamicTag().build(name="p"), "<p></p>")

            self.assertEqual(DynamicTag2().build(), "<div></div>")
            self.assertEqual(DynamicTag2().build(name="p"), "<p></p>")
            self.assertEqual(DynamicTag2().build(name="p", add="Hello Autumn"), "<p>Hello Autumn</p>")

            self.assertEqual(DynamicTag3().build(), "<div testing></div>")
            self.assertEqual(DynamicTag3().build(name="p"), "<p testing></p>")
            self.assertEqual(DynamicTag3().build(name="p", testing="abc"), '<p testing="abc"></p>')
