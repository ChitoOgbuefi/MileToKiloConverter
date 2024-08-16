from tkinter import *

#Window
window = Tk()
window.title("Metric Converter")
window.minsize(width = 500, height = 100)
window.config(padx = 60, pady = 30)

#Labels
convert_unit = Label(text = "Miles", font = ("Arial", 24))
convert_unit.grid(column = 2, row = 0)
converted_unit = Label(text = "Kms", font = ("Arial", 24))
converted_unit.grid(column = 2, row = 1)
equal = Label(text = "Is Equal to", font = ("Arial", 24))
equal.grid(column = 0, row = 1)
measurement = Label(text = 0, font = ("Arial", 24))
measurement.grid(column = 1, row = 1)

#Input
input = Entry(width = 24)
input.grid(column = 1, row = 0)

#Button
def button_clicked():
    converted = int(input.get()) * 1.6
    measurement["text"] = int(converted)

calculate = Button(text = "Calculate", command = button_clicked)
calculate.grid(column = 1, row = 2)

#Loop
window.mainloop()

