import shutil
import os

def move(src, dest):
    for files in os.listdir(src):
        if files.endswith(".txt"):
            shutil.move(src + files,dest)
    print (dest)
    print os.listdir(dest)
    

move("C:/Users/Student/Desktop/Folder A/","C:/Users/Student/Desktop/Folder B")
