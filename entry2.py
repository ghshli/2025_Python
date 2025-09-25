from tkinter import *

def submit():
    name = entry_name.get()
    age = entry_age.get()
    print("이름:", name)
    print("나이:", age)

root = Tk()
root.geometry("300x200")