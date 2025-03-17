import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("here is a textnode", TextType.TEXT)
        node2 = TextNode("here is a textnode", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_texttype(self):
        node = TextNode("here is a textnode", TextType.BOLD)
        node2 = TextNode("here is a textnode", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_texttype2(self):
        node = TextNode("here is a textnode", TextType.TEXT)
        node2 = TextNode("ouais", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("here is a textnode", TextType.ITALIC, "https://textnode.fr")
        node2 = TextNode("here is a textnode", TextType.ITALIC, "https://textnode.fr")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
