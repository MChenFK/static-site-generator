import os
import shutil

from copy_static import copy_directory
from generate_page import generate_pages_recursive

static = "./static"
public = "./public"

dir_path_content = "content"
template_path = "template.html"
dest_dir_path = "public"

def main():
    copy_directory(static, public)
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)


if __name__=="__main__":
    main()