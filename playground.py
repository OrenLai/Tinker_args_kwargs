#
# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#
#     return total
#
#
# print(add(1, 3, 5, 7))

from tkinter import *

screen = Tk()
screen.minsize(width=800, height=600)

my_label = Label(text="I am a label")
# to let the label actually show on the screen
my_label.grid(row=0, column=0)


# button
def on_click():
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = new_text


button = Button(text="click me", command=on_click)
button.grid(row=1, column=1)

new_button = Button(text="new button", command=on_click)
new_button.grid(row=0, column=2)

input = Entry(width=10)
input.grid(row=2, column=3)

screen.mainloop()
