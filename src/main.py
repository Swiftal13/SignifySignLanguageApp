import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import modelCapture

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

        self.camera = modelCapture.Camera() # Create camera object
        self.cameraRunning = False # Flag to track camera state
        self.cameraUpdateId = None # Store the after callback ID

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
        self.middleFrame = tk.Frame(self, bg=blue, height=40)
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
        # Start Button
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

        # Options Button
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

        # Camera Button
        self.cameraButton = tk.Button(
            self.buttonFrame, 
            text="Camera", 
            font=font, 
            bg=grey, 
            fg=lightGrey, 
            width=9, height=1,
            bd=0, highlightthickness=0,
            command=self.toggleCamera
        )
        self.cameraButton.pack(pady=3)


    # Button Functions
    def onStart(self):
        print("Start button clicked!")

    def onOptions(self):
        print("Options button clicked!")

    # Camera Functions
    def updateCamera(self):
        if not self.cameraRunning:
            return
       
        frame = self.camera.getFrame()
        if frame is None or frame.size ==0:
            print("Warming: No frame captured!")

        else:
            frame = Image.fromarray(frame)
            frame = frame.resize((1000,500)) # Resize the frame
            frameTk = ImageTk.PhotoImage(frame) # Convert to Tkinter PhotoImage
            self.cameraLabel.configure(image=frameTk)
            self.cameraLabel.image = frameTk

        self.cameraUpdateId = self.after(10, self.updateCamera) # Update every 10ms

    def toggleCamera(self):
        if not self.cameraRunning:  # If camera is not running
            self.cameraRunning = True
            self.updateCamera()  # Resume the update loop
            print("Camera started")
        else:
            self.cameraRunning = False
            if self.cameraUpdateId is not None:
                self.after_cancel(self.cameraUpdateId)
                self.cameraUpdateId = None
            # Instead of releasing the camera, just clear the display
            self.cameraLabel.configure(image="")
            self.cameraLabel.image = None 
            print("Camera stopped")



    def closeCamera(self): 
        self.cameraRunning = False
        if self.cameraUpdateId is not None:
            self.after_cancel(self.cameraUpdateId)
            self.cameraUpdateId = None
        self.camera.release()
        self.destroy()





if __name__ == "__main__":
    app = Signify()
    app.protocol("WM_DELETE_WINDOW", app.closeCamera)
    app.mainloop()
