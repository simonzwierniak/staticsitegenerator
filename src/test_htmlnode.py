import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://internanews.substack.com"},
        )
        self.assertEqual(
                node.props_to_html(),
                ' class="greeting" href="https://internanews.substack.com"',
            )
        
    def test_values(self):
        node = HTMLNode(
            "sup",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "sup",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
        
if __name__ == "__main__":
    unittest.main()

