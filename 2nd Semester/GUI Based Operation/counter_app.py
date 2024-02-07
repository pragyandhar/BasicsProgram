import tkinter as tk

root = tk.Tk()
root.geometry("200x200")
root.title("Counter Application")
root.minsize(50, 100)

# Global Initialisation
var = tk.IntVar(value=0)
# Actions
def add():
    data = var.get()+1
    var.set(data)
    if data >= 10:
        lb.config(fg='red')
    else:
        lb.config(fg='green')
    # lb.config(text=lb.cget('text')+1, fg="green")
def sub():
    data = var.get()-1
    if data >= 0:
        var.set(data)
    if data >= 10:
        lb.config(fg='red')
    else:
        lb.config(fg='green')
    # lb.config(text=lb.cget('text')-1, fg="red")

lb = tk.Label(root, textvariable=var, font=('bold',30), fg="green")
lb.pack()
button1 = tk.Button(root, text=" Increment ", command=add, fg="green")
button1.pack(side=tk.LEFT, ipadx=10, ipady=10, padx=10, pady=10)
button2 = tk.Button(root, text=" Decrement ", command=sub, fg='red')
button2.pack(side=tk.CENTER, ipadx=10, ipady=10, padx=10, pady=10)

root.mainloop()