import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
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