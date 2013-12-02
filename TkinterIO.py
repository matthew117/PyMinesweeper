from Tkinter import *

root = Tk()
#root.geometry("600x600+300+300")
root.title("Minesweeper")

for y in range(0, 8):
    for x in range(0, 8):
        Button(root, text="({0},{1})".format(x,y)).grid(row=y, column=x)

root.mainloop()

