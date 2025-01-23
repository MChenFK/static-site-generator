from textnode import *

def main():
    textnode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(textnode.__repr__())

if __name__=="__main__":
    main()