import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_value_required(self):
        node = LeafNode(tag=None, value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = LeafNode(tag=None, value="test value")
        associated_value = node.to_html()
        self.assertEqual(associated_value, "test value")

    def test_to_html_no_props(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        render = node.to_html()
        self.assertEqual(render, "<p>This is a paragraph of text.</p>")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        render = node.to_html()
        self.assertEqual(render, f'<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()