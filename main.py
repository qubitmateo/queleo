from tkinter import *

bg_color = '#2e2a78'
color2 = '#f2ff66'

root = Tk()  # create a root widget
root.title("queleo")
root.configure(background=bg_color)
root.minsize(1000, 700)  # width, height
root.maxsize(1000, 700)
root.geometry("300x300+50+50")  # width x height + x + y

# Create Label in our window
text = Label(root, text="QueLeo", foreground="white", background=bg_color, font=("Times New Roman", 32))
text.pack()
text2 = Label(root, text="Agrega libros.", foreground=color2, background=bg_color, font=("Times New Roman", 25))
text2.pack()
root.mainloop()