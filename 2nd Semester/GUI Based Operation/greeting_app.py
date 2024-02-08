import tkinter as tk
class app:
    def __init__(self, mainwindow) -> None:
        mainwindow.geometry("300x300")
        mainwindow.title("Greeting Application")
        mainwindow.minsize(100, 100)
        
        self.lb = tk.Label(root, text="Enter your name")
        self.lb.pack()

        self.name = tk.Entry(root)
        self.name.pack()

        self.b = tk.Button(root, text="Greet", command=self.action)
        self.b.pack()
        self.outLabel = tk.Label(mainwindow, text="")
        self.outLabel.pack()

    def action(self):
        data = self.name.get()
        self.outLabel.config(text="Welcome, Welcome, Welcome " + data)
        self.name.delete(0, tk.END)
root = tk.Tk()
exe = app(root)
root.mainloop()