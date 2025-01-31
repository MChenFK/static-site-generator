import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)


class TestMarkdownToHTML(unittest.TestCase):
    # Test markdown_to_blocks
    def test_markdown_to_blocks_various_sizes_and_newlines(self):
        md = """
A




A
A




* A
* A
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "A",
                "A\nA",
                "* A\n* A",
            ],
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    
    # Test block_to_block_types:
    def test_block_to_block_types(self):
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        
    def test_multiple_heading_layers(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "## heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "### heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "#### heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "##### heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "###### heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
    
    def test_too_many_heading_layers(self):
        block = "####### heading"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()