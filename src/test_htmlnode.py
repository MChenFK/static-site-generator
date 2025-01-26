import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    # Test HTMLNode:
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

    # Test LeafNode:
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

    #Test ParentNode
    def test_no_tag(self):
        node = ParentNode(
            tag=None,
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children(self):
        node = ParentNode("p", children=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children_list(self):
        node = ParentNode("p", children=[])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_node_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        render = node.to_html()
        self.assertEqual(render, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
            ],
        )

        render = node.to_html()
        self.assertEqual(render, "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")


if __name__ == "__main__":
    unittest.main()