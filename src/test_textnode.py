import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("testnode", TextType.BOLD)
        node2 = TextNode("testnode", TextType.BOLD)
        self.assertEqual(node,node2)
    def test_not_eq_type(self):
        node = TextNode("testnode", TextType.BOLD)
        node2 = TextNode("testnode", TextType.ITALIC)
        self.assertNotEqual(node,node2)
    def test_not_eq_url(self):
        node = TextNode("testnode", TextType.BOLD)
        node2 = TextNode("testnode", TextType.BOLD,"www.url.com")
        self.assertNotEqual(node,node2)
if __name__ == "__main__":
    unittest.main()