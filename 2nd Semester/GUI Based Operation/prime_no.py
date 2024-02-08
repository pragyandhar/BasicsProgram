import tkinter as tk
class prime:
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
        data = int(self.input_box.get())
        if data == 1:
            self.input_box.config(text="1 neither prime nor composite")
        else:
            for i in range(2, data):
                if (data%i==0):
                    self.out.config(text="The number is not prime", fg="red")
                    break
                else:
                    self.out.config(text="The number is a prime", fg=green)
                    break

root = tk.Tk()
exe = prime(root)
root.mainloop()