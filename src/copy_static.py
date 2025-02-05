import os
import shutil

def copy_directory(source, destination):
    if os.path.exists(destination):
        print("Deleting directory...")
        shutil.rmtree(destination)

    print("Copying files to directory...")
    os.mkdir(destination)
    
    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        destination_path = os.path.join(destination, filename)
        print(f" * {source_path} -> {destination_path}")
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            copy_directory(source_path, destination_path)