import shutil
import os
import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)

def copyMe(src, dest):
    for file in os.listdir(src):
        if mtime > ago and file.endswith(".txt"):
            shutil.copy(src + file,dest)

for root,dirs,file in os.walk('C:/Users/Student/Desktop/FilesToCheck/'):  
    for fname in file:
        path = os.path.join(root, fname)
        st = os.path.getmtime(path)    
        mtime = dt.datetime.fromtimestamp(st)
        if mtime > ago:
            copyMe('C:/Users/Student/Desktop/FilesToCheck/', 'C:/Users/Student/Desktop/DestinationFolder')            


#os.path.getmtime(path)
#os.stat(path) 
