import tkinter as tk
class triangle:
    def __init__(self, mainwindow) -> None:
        self.mainwindow = mainwindow
        mainwindow.geometry("300x300")
        mainwindow.title("Prime or not")
        mainwindow.minsize(100, 100)

        self.input_text = tk.Label(mainwindow, text="Input any number")
        self.input_text.pack()
        self.input_box = tk.Entry(mainwindow)
        self.input_box.pack()
        self.button = tk.Button(mainwindow, text="CHECK", command=self.calc)
        self.button.pack()
        self.out = tk.Label(mainwindow, text="")
        self.out.pack()
    def calc(self):
        data = self.input_box.get()
        for i in range(1, data):
            for j in range(i):
                st+="*"
            st+="\n"
        self.out.config(text=st)

root = tk.Tk()
exe = triangle(root)
root.mainloop()