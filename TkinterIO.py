from Tkinter import *

# Difficult to change behaviour based on which button is clicked as command has no reference to self
def onClick():
    print("Hello")

root = Tk()
root.geometry("600x600+300+300")
root.title("Minesweeper")

for y in range(0, 8):
    for x in range(0, 8):
        b = Button(root, text="({0},{1})".format(x,y), command=onClick)
        b.grid(row=y, column=x)

root.mainloop()

