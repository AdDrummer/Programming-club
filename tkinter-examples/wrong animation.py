from tkinter import *


root=Tk()
c = Canvas(root, width=1000, height=1000)
c.pack()

oval = c.create_oval(0, 0, 50, 50, fill='yellow')
c.update()
c.after(1000)
c.move(oval, 10, 10)
c.update()
c.after(1000)
c.move(oval, 10, 10)
c.update()
c.after(1000)
c.move(oval, 10, 10)
c.update()
c.after(1000)
c.move(oval, 10, 10)
c.update()
c.after(1000)
c.move(oval, 10, 10)
c.update()
c.after(1000)
c.move(oval, 10, 10)
c.update()
c.after(1000)
c.move(oval, 10, 10)
c.update()

root.mainloop()
