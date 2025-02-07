import os, os.path
import shutil
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
    dest_path = dest_path[:-2] + "html"
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
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, filename)
        destination_path = os.path.join(dest_dir_path, filename)
        print(f" * {source_path} -> {destination_path}")
        if os.path.isfile(source_path):
            if source_path[-3:] == ".md":
                generate_page(source_path, template_path, destination_path)
        else:
            generate_pages_recursive(source_path, template_path, destination_path)