from textnode import TextNode, TextType

def main():
    node = TextNode("here is a textnode", TextType.LINK, "internanews.substack.com")
    print(node)

main()