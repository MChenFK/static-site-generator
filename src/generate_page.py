import os, os.path
from markdown_blocks import markdown_to_html_node
from htmlnode import *

def extract_title(markdown):
    if len(markdown) == 0:
        raise Exception("Markdown must not be empty")
    lines = markdown.split("\n")
    for line in lines:
        if line[:2] == "# ":
            return line.strip("# ")
    raise Exception("Markdown must have title)")

def safe_open_w(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, mode='r')
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, mode='r')
    template = template_file.read()
    template_file.close()

    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_string)

    with safe_open_w(dest_path) as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    pass