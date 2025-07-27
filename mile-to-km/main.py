from tkinter import *

def convert():
    miles = float(mile.get())
    km["text"] = miles * 1.60934

window = Tk()
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)
window.title("Mile to Km Converter")

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_mile = Label(text="Miles")
label_mile.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

km = Label(text=0)
km.grid(column=1, row=1)

mile = Entry()
mile.insert(END, string="0")
mile.grid(column=1, row=0)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
