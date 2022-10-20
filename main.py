
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456789"
)

print(mydb)

project = Tk()
project.title("Project")
project.geometry("500x500")
project.iconbitmap("assets/images/icon.ico")
#  label
label = Label(project, text="Hello World", font= 'CloudLight 20')
mysql = Label(project, text=mydb, font= 'CloudLight 10')
label.pack(padx=10, pady=20)
mysql.pack(padx=10, pady=20)

#  button
button = Button(project, text="Click Me")
button.pack()


project.mainloop()

 