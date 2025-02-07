import unittest

from generate_page import *

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        result = extract_title("# Hello")
        self.assertEqual(result,  "Hello")

    def test_extract_title_second_line(self):
        result = extract_title("Line 1\n# Line 2")
        self.assertEqual(result,  "Line 2")

    def test_extract_title_empty(self):
        with self.assertRaises(Exception):
            extract_title("")

    def test_extract_title_no_title(self):
        with self.assertRaises(Exception):
            extract_title("Line 1\nLine 2")

if __name__ == "__main__":
    unittest.main()