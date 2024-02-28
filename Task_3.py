from tkinter import *
import random, string

interface = Tk()
interface.geometry("200x200+370+20")
interface.config(background="white")
interface.title("Password_generator_Abhipriya")

title = StringVar()
label = Label(interface, textvariable=title).pack()
title.set("Strength of password:")


def selection():
    selection = choice.get()


choice = IntVar()
button_1 = Radiobutton(interface, text="Weak", variable=choice, value=1, command=selection).pack(anchor=CENTER)
button_2 = Radiobutton(interface, text="Medium", variable=choice, value=2, command=selection).pack(anchor=CENTER)
button_3 = Radiobutton(interface, text="Strong", variable=choice, value=3, command=selection).pack(anchor=CENTER)
labelchoice = Label(interface)
labelchoice.pack()

length_choice = StringVar()
length_choice.set("Password length")
length_title = Label(interface, textvariable=length_choice).pack()

val = IntVar()
passlength = Spinbox(interface, from_=6, to_=24, textvariable=val, width=15).pack()


def callback():
    lsum.configtext = passgenButton()


passgenButton = Button(interface, text="Generate Password", border=3, height=1, command=callback, pady=3)
passgenButton.pack()
password = str(callback)

lsum = Label(interface, text="")
lsum.pack(side=BOTTOM)

Weak = string.ascii_uppercase + string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation
Medium = string.ascii_uppercase + string.ascii_lowercase + string.digits + numbers
Strong = Weak + Medium + symbols + numbers


def passgenButton():
    if choice.get() == 1:
        return "".join(random.sample(Weak, val.get()))
    if choice.get() == 2:
        return "".join(random.sample(Medium, val.get()))
    if choice.get() == 3:
        return "".join(random.sample(Strong, val.get()))


interface.mainloop()