import pyautogui
import time
from tkinter import filedialog

def screenshot():
    name = int(round(time.time() * 1000))
    name = f'{name}.png'
    directory_path = filedialog.askdirectory()
    name = f'{directory_path}/{name}'
    print(name) 
    img = pyautogui.screenshot(name)
    img.show()

if __name__ == '__main__':
    screenshot()



