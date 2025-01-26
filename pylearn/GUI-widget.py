from IPython.display import display
display(Image(filename='image.jpg'))
import tkinter as tk
root=tk.Tk()
root.title("GUI")
root.geometry("500x500")
tk.Label(root,text="Hello World").pack()login-gui.py

root.mainloop() #to run the window

