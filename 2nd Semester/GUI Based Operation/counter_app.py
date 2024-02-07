import tkinter as tk
class Counter:
    def __init__(self, mainwindow) -> None:
        self.mainwindow = mainwindow
        mainwindow.geometry("200x200")
        mainwindow.title("Counter Application")
        mainwindow.minsize(50, 100)
        # Global Initialisation
        self.var = tk.IntVar(value=0)
        self.lb = tk.Label(root, textvariable=self.var, font=('bold',30), fg="green")
        self.lb.pack()
        self.button1 = tk.Button(root, text=" Increment ", command=self.add, fg="green")
        self.button1.pack(side=tk.LEFT, ipadx=10, ipady=10, padx=10, pady=10)
        self.button2 = tk.Button(root, text=" Decrement ", command=self.sub, fg='red')
        self.button2.pack(side=tk.RIGHT, ipadx=10, ipady=10, padx=10, pady=10)

    def add(self):
        data = self.var.get()+1
        self.var.set(data)
        if data >= 10:
            self.lb.config(fg='red')
        else:
            self.lb.config(fg='green')
        # lb.config(text=lb.cget('text')+1, fg="green")
    
    def sub(self):
        data = self.var.get()-1
        if data >= 0:
            self.var.set(data)
        if data >= 10:
            self.lb.config(fg='red')
        else:
            self.lb.config(fg='green')
        # lb.config(text=lb.cget('text')-1, fg="red")
            


# Main Window
root = tk.Tk()
exe = Counter(root)
root.mainloop() # To hold the interface