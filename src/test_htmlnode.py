import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_default_none(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(),  'href="https://www.google.com" target="_blank"')

    def test_repr(self):
        child = HTMLNode()
        children = [child]
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(tag="tag", value="value", children=children, props=props)
        self.assertEqual(node.__repr__(),  f'HTMLNode(tag, value, [HTMLNode(None, None, None, None)], {props})')


if __name__ == "__main__":
    unittest.main()