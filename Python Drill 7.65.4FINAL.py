import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror
import shutil
import os
import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.fileCheck = tk.Button(self)
        self.fileCheck["text"] = "Click for file check"
        self.fileCheck["command"] = self.checkFiles
        self.fileCheck.pack(side="bottom")

        self.src=StringVar()
        label = Entry(self, textvariable = self.src)
        label.pack() 
        self.browseSource = Button(self, text="Browse source", command=self.load_file_src, width=30)
        self.browseSource.pack(side="top")

        self.dst=StringVar()
        label = Entry(self, textvariable = self.dst)
        label.pack()
        self.browseDst = Button(self, text="Browse destination", command=self.load_file_dst, width=30)
        self.browseDst.pack(side="top")

    def load_file_src(self):
        self.fnameS = askdirectory(title=(("All folders", "*.*")))
        self.src.set(self.fnameS)
        print (self.fnameS)
        
    def load_file_dst(self):
         self.fnameD = askdirectory(title=(("All folders", "*.*")))
         self.dst.set(self.fnameD)
         print (self.fnameD)

    def checkFiles(self):           
        for file in os.listdir(self.fnameS):
            if file.endswith('.txt'):
                src_name = os.path.join(self.fnameS,file)
                ftime = os.path.getmtime(src_name)
                mtime = dt.datetime.fromtimestamp(ftime)
                if mtime > ago:   
                    shutil.copy(src_name,self.fnameD)
                    print("Files have been checked & copied!")
                    print (file)

                    
root = tk.Tk()
root.title("FILE MAGIC COPIER!!!1!")
root.geometry("400x200")
app = Application(master=root)
app.mainloop()
