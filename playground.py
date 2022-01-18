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
my_label.pack()


# button
def on_click():
    print("I got clicked")
    my_label["text"] = "button got clicked"


button = Button(text="click me", command=on_click)
button.pack()

screen.mainloop()
