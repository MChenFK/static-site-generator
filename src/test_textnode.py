import unittest

from textnode import *
from htmlnode import *


class TestTextNode(unittest.TestCase):
    # Test TextNode
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_default_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    # Test text_node_to_html_node
    def test_text_to_html_node(self):
        node = TextNode("Raw text", TextType.TEXT)
        new_node = text_node_to_html_node(node)
        self.assertEqual(new_node.tag, None)
        self.assertEqual(new_node.value, "Raw text")

    def test_bold_to_html_node(self):
        node = TextNode("Raw text", TextType.BOLD)
        new_node = text_node_to_html_node(node)
        self.assertEqual(new_node.tag, "b")
        self.assertEqual(new_node.value, "Raw text")

    def test_image_to_html_node(self):
        node = TextNode("Raw text", TextType.IMAGE, "https://google.com")
        new_node = text_node_to_html_node(node)
        self.assertEqual(new_node.tag, "img")
        self.assertEqual(new_node.value, "")
        self.assertEqual(new_node.props, {"src": "https://google.com", "alt": "Raw text"})


if __name__ == "__main__":
    unittest.main()