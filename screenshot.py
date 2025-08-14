import time
import pyautogui 
import tkinter as tk 

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'D:/Python/Screenshots data/{}.png'.format(name)
    time.sleep(1)
    img = pyautogui.screenshot(name) 
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text = "Take Screenshot", command = screenshot)
button.pack(side=tk.LEFT)
close = tk.Button(frame, text = "Close", command=root.quit)
close.pack(side=tk.LEFT)

root.mainloop()