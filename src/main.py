import os
import shutil

from copy_static import copy_directory

static = "./static"
public = "./public"

def main():
    copy_directory(static, public)

if __name__=="__main__":
    main()