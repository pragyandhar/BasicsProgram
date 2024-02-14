#You have to create a GUI application for calculating the Body Mass Index (BMI) of a person. The application should have the following features: One Height and Weight Entry Box and a Calculate Button. When the user enters the height and weight and clicks the Calculate button, the application should calculate the BMI and display the result in a Result Entry Box. The formula for calculating BMI is: BMI = weight / (height * height) where weight is in kilograms and height is in meters. The application should also have a title "Body Mass Index" and should be of size 500x500.
import tkinter as tk
from tkinter.messagebox import *
class bmi:
    def __init__(self, mainwindow) -> None:
            #First Label and Textbox
        self.lb1 = tk.Label(mainwindow, text='Height(m)')
        self.lb1.grid(row=0, column=0)
        self.tb1 = tk.Entry()
        self.tb1.grid(row=0,column=1)

            #Second Label and Textbox
        self.lb2 = tk.Label(mainwindow, text='Weight(m)')
        self.lb2.grid(row=1, column=0)
        self.tb2 = tk.Entry()
        self.tb2.grid(row=1,column=1)

            #Result Label and Textbox
        self.lb3 = tk.Label(mainwindow, text='Result')
        self.lb3.grid(row=2, column=0)
        self.tb3 = tk.Entry()
        self.tb3.grid(row=2,column=1)
            
            #Creating Button
        self.bt1 = tk.Button(mainwindow, text='Calculate', command=self.calc)
        self.bt1.grid(row=3, column=1)
        

#FUNCTIONS
    def calc(self):
        data1 = float(self.tb1.get())
        data2 = float(self.tb2.get())
        result = data2 / (data1 * data1)
        self.tb3.insert(0, str(result))
        showinfo("Result", f"Your BMI is {result}")

#MAIN WINDOW
root = tk.Tk()
root.title("Body Mass Index")
root.geometry('500x500')
exe = bmi(root)
root.mainloop()