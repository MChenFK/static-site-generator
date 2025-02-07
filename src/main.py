import os
import shutil

from copy_static import copy_directory
from generate_page import generate_page

static = "./static"
public = "./public"

from_path = "content/index.md"
template_path = "template.html"
dest_path = "public/index.html"

def main():
    copy_directory(static, public)
    generate_page(from_path, template_path, dest_path)


if __name__=="__main__":
    main()