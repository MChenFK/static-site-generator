import os
import shutil

def copy_directory(source, destination):
    if os.path.exists(destination):
        print("Deleting directory...")
        shutil.rmtree(destination)

    print("Copying files to directory...")
    os.mkdir(destination)
    
    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        dest_path = os.path.join(destination, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_directory(from_path, dest_path)