import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror
import shutil
import os
import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)

import sqlite3
#create database
conn = sqlite3.connect('fileCheckRecord.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS fileCheckRecord
             (Last_Update)''')

# Save (commit) the changes
conn.commit()
            
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #file checking button
        self.fileCheck = tk.Button(self)
        self.fileCheck["text"] = "Click for file check"
        self.fileCheck["command"] = self.checkFiles
        self.fileCheck.pack(side="bottom")

        #"source" entry box
        self.src=StringVar()
        label = Entry(self, textvariable = self.src)
        label.pack() 
        self.browseSource = Button(self, text="Browse source", command=self.load_file_src, width=30)
        self.browseSource.pack(side="top")

        #"destination" entry box
        self.dst=StringVar()
        label = Entry(self, textvariable = self.dst)
        label.pack()
        self.browseDst = Button(self, text="Browse destination", command=self.load_file_dst, width=30)
        self.browseDst.pack(side="top")

        #"last update" box
        self.lstUpdt=StringVar()
        label = Entry(self, textvariable = self.lstUpdt)
        label.pack() 
        self.lastUpdate = Button(self, text="Last Update", command=self.lastUpdate_str, width=30)
        self.lastUpdate.pack(side="bottom")

    def load_file_src(self):
        self.fnameS = askdirectory(title=(("All folders", "*.*")))
        self.src.set(self.fnameS)
        print (self.fnameS)
        
    def load_file_dst(self):
         self.fnameD = askdirectory(title=(("All folders", "*.*")))
         self.dst.set(self.fnameD)
         print (self.fnameD)

    def lastUpdate_str(self):
        cursor = c.execute('''SELECT MAX(Last_Update) FROM fileCheckRecord''')
        self.max_time = cursor.fetchone()
        self.lstUpdt.set(self.max_time)
        print (self.max_time)

    def checkFiles(self):           
        for file in os.listdir(self.fnameS):
            if file.endswith('.txt'):
                src_name = os.path.join(self.fnameS,file)
                ftime = os.path.getmtime(src_name)
                mtime = dt.datetime.fromtimestamp(ftime)
                if mtime > ago:   
                    shutil.copy(src_name,self.fnameD)
                    c.execute("INSERT INTO fileCheckRecord (Last_Update) VALUES (?)",(dt.datetime.now(),))
                    print("Files have been checked & copied!")
                    print (file)
                    
root = tk.Tk()
root.title("FILE MAGIC COPIER!!!!")
root.geometry("400x200")
app = Application(master=root)
app.mainloop()
