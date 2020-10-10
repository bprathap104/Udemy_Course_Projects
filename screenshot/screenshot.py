import pyautogui
import time
from tkinter import Tk, Label, Frame, filedialog, Button, LEFT
import tkinter

def screenshot():
    name = int(round(time.time() * 1000))
    name = f'{name}.png'
    directory_path = filedialog.askdirectory()
    name = f'{directory_path}/{name}'
    print(name) 
    img = pyautogui.screenshot(name)
    img.show()

if __name__ == '__main__':
    root = Tk()
    frame = Frame(root)
    frame.pack()
    button = Button(
        frame,
        text="Take Screenshot",
        command=screenshot
    )
    button.pack(side=LEFT)
    close = Button(
        frame,
        text="Quit",
        command=quit)
    close.pack(side=LEFT)
    root.mainloop()

    root.mainloop()


