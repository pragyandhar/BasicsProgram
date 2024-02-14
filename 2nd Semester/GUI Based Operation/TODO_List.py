#You have to make a TO-DO List GUI Application where you need to add items to the list and delete items from the list. The application should have the following features: One Entry Box and an Add Item Button. When the user enters the item and clicks the Add Item button, the item should be added to the list. The application should also have a Delete Item Button and a Delete All Items Button. When the user selects an item from the list and clicks the Delete Item button, the selected item should be deleted from the list. When the user clicks the Delete All Items button, all the items should be deleted from the list. The application should also have a title "TO DO LIST" and should be of size 400x300 using class and object.

import tkinter as tk
class todo:
    def add(self):
        data = self.entry.get()
        self.lstbx.insert(tk.END, data)
        self.entry.delete(0, tk.END)
    
    def delete(self):
        select_index = self.lstbx.curselection()
        self.lstbx.delete(select_index)
    
    def deleteall(self):
        self.lstbx.delete(0, tk.END)


    def __init__(self, mainwindow) -> None:
        self.mainwindow = mainwindow
        mainwindow.title('TO DO LIST')
        mainwindow.geometry('400x300')

        self.lb1 = tk.Label(mainwindow, text='Item')
        self.lb1.grid(row=0, column=0)
        self.entry = tk.Entry(mainwindow)
        self.entry.grid(row=0, column=1)
        self.bt1 = tk.Button(mainwindow, text='Add Item', command=self.add)
        self.bt1.grid(row=0, column=2)

        self.lstbx = tk.Listbox(mainwindow, width=20)
        self.lstbx.grid(row=1, column=0, columnspan=2)

        self.bt2 = tk.Button(mainwindow, text='Delete Item', command=self.delete)
        self.bt2.grid(row=2, column=0)

        self.bt3 = tk.Button(mainwindow, text='Delete All Items', command=self.deleteall)
        self.bt3.grid(row=2, column=1)

root = tk.Tk()
exe = todo(root)
root.mainloop()