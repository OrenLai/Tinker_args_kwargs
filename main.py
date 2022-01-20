from tkinter import *

screen = Tk()
screen.title("Mile to Km Converter")
screen.config(padx=30, pady=30)

text = Entry()
text.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_result = Label(text="0")
label_result.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)


def miles_to_km():
    label_result["text"] = round(float(text.get()) * 1.609)


button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

screen.mainloop()
