import tensorflow as ts
import numpy as np
import cv2 as cv
from tkinter import *
import tkinter

#colours
lightGrey = "#D9D9D9"
grey = "#3A3A3A"
darkGrey = "#212121"
blue = "#6E6C80"

#fonts
Font = ("Arabic Transparent", 15)
FontBold = ("Arabic Transparent", 15)

#class

class Signify(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Signify")
        self.geometry("1000x600")
        self.configure(bg=lightGrey)

        self.label = Label(self, text="Welcome to Signify", font=FontBold, bg=lightGrey, fg=darkGrey)
        self.label.pack(pady=20)

        self.button = Button(self, text="Click Me", font=Font, bg=blue, fg=lightGrey, command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button clicked!")


if __name__ == "__main__":
    app = Signify()
    app.mainloop()
