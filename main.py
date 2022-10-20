
from tkinter import *

import pymysql

con = pymysql.connect(host="localhost", database="pythonlab", user="root", password="123456789", charset="utf8")
print(con)

project = Tk()
project.title("Project")
project.geometry("500x500")
project.iconbitmap("assets/images/icon.ico")
#  label
label = Label(project, text="Hello World", font= 'CloudLight 20')
label.pack(padx=10, pady=20)

#  button
button = Button(project, text="Click Me")
button.pack()


project.mainloop()

 