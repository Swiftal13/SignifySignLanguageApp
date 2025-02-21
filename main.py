import tkinter as tk
from tkinter import *

# Colours
lightGrey = "#D9D9D9"
grey = "#3A3A3A"
darkGrey = "#212121"
blue = "#6E6C80"

# Fonts
font = ("Arabic Transparent", 13)
fontBold = ("Arabic Transparent", 12, "bold")

class Signify(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Signify")
        self.geometry("1000x650")
        self.configure(bg=lightGrey)

        # Top Frame
        self.topFrame = tk.Frame(self, bg=lightGrey)
        self.topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.cameraLabel = tk.Label(
            self.topFrame, 
            text="camera footage", 
            font=fontBold, 
            bg=lightGrey, 
            fg="red"
        )
        self.cameraLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Middle Frame
        self.middleFrame = tk.Frame(self, bg=blue, height=50)
        self.middleFrame.pack(side=tk.TOP, fill=tk.X)

        self.wordLabel = tk.Label(
            self.middleFrame, 
            text="Word / letter", 
            font=fontBold, 
            bg=blue, 
            fg=lightGrey
        )
        self.wordLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Bottom Frame
        self.bottomFrame = tk.Frame(self, bg=darkGrey, height=120)
        self.bottomFrame.pack(side=tk.BOTTOM, fill=tk.X)

        # Button Frame
        self.buttonFrame = tk.Frame(self.bottomFrame, bg=darkGrey)
        self.buttonFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Buttons
        self.startButton = tk.Button(
            self.buttonFrame, 
            text="Start", 
            font=font, 
            bg=grey, 
            fg=lightGrey, 
            width=9, height=1,
            bd=0, highlightthickness=0,
            command=self.onStart
        )
        self.startButton.pack(pady=3)

        self.optionsButton = tk.Button(
            self.buttonFrame, 
            text="Options", 
            font=font, 
            bg=grey, 
            fg=lightGrey, 
            width=9, height=1,
            bd=0, highlightthickness=0,
            command=self.onOptions
        )
        self.optionsButton.pack(pady=3)

        self.cameraButton = tk.Button(
            self.buttonFrame, 
            text="Camera", 
            font=font, 
            bg=grey, 
            fg=lightGrey, 
            width=9, height=1,
            bd=0, highlightthickness=0,
            command=self.onCamera
        )
        self.cameraButton.pack(pady=3)

    def onStart(self):
        print("Start button clicked!")

    def onOptions(self):
        print("Options button clicked!")

    def onCamera(self):
        print("Camera button clicked!")

if __name__ == "__main__":
    app = Signify()
    app.mainloop()
