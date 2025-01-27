from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("Invalid Markdown syntax")
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_node[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split_node[i], text_type))

        new_nodes.extend(split_nodes)
    return new_nodes

        