from tkinter import *
import math as m

interface = Tk()
interface.geometry("345x430+450+20")
interface.config(background="white")
interface.title("Calculator_Abhipriya")
interface.resizable(False, False)


def close():
    interface.destroy()


def clear():
    global entry_text
    entry_string.set("")
    entry_text = ""


def back():
    last_num = len(entry.get()) - 1
    entry.delete(last_num)


def press(num):
    global entry_text
    entry_text = entry_text + str(num)
    entry_string.set(entry_text)


def equals():
    global entry_text
    total = str(eval(entry_text))
    entry_string.set(total)


entry_text = ""
entry_string = StringVar()
entry = Entry(interface, textvariable=entry_string, fg="white", bg="black", border=0, font=("Calibri", 25))
entry.grid(columnspan=4, ipady=10)

font_variable = ("Calibri", 18)
button_1 = Button(interface, text="1", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("1"))
button_1.grid(row=1, column=0, sticky=E + W, ipady=5)
button_2 = Button(interface, text="2", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("2"))
button_2.grid(row=1, column=1, sticky=E + W, ipady=5)
button_3 = Button(interface, text="3", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("3"))
button_3.grid(row=1, column=2, sticky=E + W, ipady=5)
button_4 = Button(interface, text="4", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("4"))
button_4.grid(row=1, column=3, sticky=E + W, ipady=5)

button_5 = Button(interface, text="5", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("5"))
button_5.grid(row=2, column=0, sticky=E + W, ipady=5)
button_6 = Button(interface, text="6", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("6"))
button_6.grid(row=2, column=1, sticky=E + W, ipady=5)
button_7 = Button(interface, text="7", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("7"))
button_7.grid(row=2, column=2, sticky=E + W, ipady=5)
button_8 = Button(interface, text="8", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("8"))
button_8.grid(row=3, column=2, sticky=E + W, ipady=5)

button_9 = Button(interface, text="9", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("9"))
button_9.grid(row=3, column=0, sticky=E + W, ipady=5)
button_0 = Button(interface, text="0", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                command=lambda: press("0"))
button_0.grid(row=3, column=1, sticky=E + W, ipady=5)
button_point = Button(interface, text=".", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                    command=lambda: press("."))
button_point.grid(row=2, column=3, sticky=E + W, ipady=5)
button_plus = Button(interface, text="+", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                   command=lambda: press("+"))
button_plus.grid(row=3, column=3, sticky=E + W, ipady=5)

button_clear = Button(interface, text="C", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                    command=clear)
button_clear.grid(row=4, columnspan=2, column=0, sticky=E + W, ipady=5)
button_backspace = Button(interface, text="B", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                        command=back)
button_backspace.grid(row=4, columnspan=2, column=2, sticky=E + W, ipady=5)

button_mul = Button(interface, text="x", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                  command=lambda: press("*"))
button_mul.grid(row=5, column=0, sticky=E + W, ipady=5)
button_minus = Button(interface, text="-", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                    command=lambda: press("-"))
button_minus.grid(row=5, column=1, sticky=E + W, ipady=5)
button_div = Button(interface, text="/", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                  command=lambda: press("/"))
button_div.grid(row=5, column=2, sticky=E + W, ipady=5)
button_fact = Button(interface, text="!", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                   command=lambda: press("!"))
button_fact.grid(row=5, column=3, sticky=E + W, ipady=5)

button_equal = Button(interface, text="=", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                    command=equals)
button_equal.grid(row=6, column=0, columnspan=3, sticky=E + W, ipady=5)
button_close = Button(interface, text="close", fg="white", bg="gray11", font=font_variable, borderwidth=2, relief=GROOVE,
                    command=close)
button_close.grid(row=6, column=3, sticky=E + W, ipady=5)

interface.mainloop()