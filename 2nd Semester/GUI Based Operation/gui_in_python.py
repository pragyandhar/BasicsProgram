"""
The modules used for GUI are:
1) tkinter
2) wxpython
3) pyqt6
"""

import tkinter as tk

root = tk.Tk()
root.geometry("200x100")
root.title("First App")
root.minsize(100, 200)


# def my_fun():
#     data = lb.cget("text")
#     if data == "Hi":
#         lb.config(text="Hello")
#     else:
#         lb.config(text="Hi")

def my_fun1():
    # pass
    lb.config(text=lb.cget('text')+1, fg="green")


def my_fun2():
    lb.config(text=lb.cget('text')-1, fg="red")
    # pass


lb = tk.Label(root, text=0)
lb.pack()
# agar my_fun1 ke aage () lga diya to output "None" aayega
bt1 = tk.Button(root, text=" + ", command=my_fun1)
bt1.pack()
bt2 = tk.Button(root, text=" - ", command=my_fun2)
bt2.pack()

root.mainloop()
