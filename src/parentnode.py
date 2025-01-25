from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        if isinstance(self.children, list) and len(self.children) == 0:
            raise ValueError("All parent nodes must have children")
        return f'<{self.tag}>{"".join(list(map(lambda x: x.to_html(), self.children)))}</{self.tag}>'