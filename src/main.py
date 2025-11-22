
#def copy(source, dest):
#    if os.listdir(dest) != []:
#        print(f"{dest} is not empty, clearing {dest}")
#        shutil.rmtree(dest)
#        os.mkdir(dest)
#    print(source)
#    
#    content = os.listdir(source)
#    for file in content:
#        print(f"is: {os.path.abspath(file)}")
#        print(os.path.isfile(os.path.abspath(source + "/" +file)))
#        if os.path.isfile(os.path.abspath(source + "/" +file)):
#            print(f"copying {source}/{file}")
#            shutil.copy(f"{source}/{file}", dest)
#        else:
#            if os.path.exists(f"{dest}/{file}") == False:
#                print(f"Creating {dest}/{file}")
#                os.mkdir(f"{dest}/{file}")
#            copy(f"{source}/{file}", f"{dest}/{file}")
import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
basepath = sys.argv[1]
if basepath == "":
    basepath = "./"
def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
 
    print("Generating content...")

    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)  
    


main()