import tkinter as tk
class MyCalculator:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("my calculator")

        self.label = tk.Label(self.root, text="Hello DIP01", font='Arail')
        self.label.pack()

        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x=20, y=50)

        self.root.mainloop()

MyCalculator()
