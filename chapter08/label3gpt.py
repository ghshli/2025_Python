from tkinter import *
import os

root = Tk()
path = os.path.dirname(__file__)   # 현재 파일이 있는 폴더 경로
photo = PhotoImage(file=os.path.join(path, "dog2.gif"))
label = Label(root, image=photo)
label.pack()
root.mainloop()