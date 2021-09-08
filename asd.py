import tkinter, random

class BubbleFrame:

    def __init__(self, root):
        root.title("Math Bubbles")
        tkinter.Button(root, text="Add Bubbles", width=8, command=self.bubble).pack()
        tkinter.Button(root, text="Quit", width=8, command=quit).pack()
        self.canvas = tkinter.Canvas(root, width=800, height=650, bg = '#afeeee')
        self.canvas.pack()
        self.bubbles = {} # this will hold bubbles ids, positions and velocities

    def bubble(self):
        # add bubbles for numbers from 1 to 20
        for number in range(1, 20+1):
            xval = random.randint(5,765)
            yval = random.randint(5,615)
            s1 = self.canvas.create_oval(xval,yval,xval+30,yval+30, fill="#00ffff",outline="#00bfff",width=5)
            s2 = self.canvas.create_text(xval+15,yval+15, text=number)
            self.bubbles[(s1, s2)] = (xval, yval, 0, 0) # add bubbles to dictionary

    def loop(self, root):
        for (s1, s2), (x, y, dx, dy) in self.bubbles.items():
            # update velocities and positions
            dx += random.randint(-1, 1)
            dy += random.randint(-1, 1)
            # dx and dy should not be too large
            dx, dy = max(-5, min(dx, 5)), max(-5, min(dy, 5))
            # bounce off walls
            if not 0 < x < 770: dx = -dx
            if not 0 < y < 620: dy = -dy
            # apply new velocities
            self.canvas.move(s1, dx, dy)
            self.canvas.move(s2, dx, dy)
            self.bubbles[(s1, s2)] = (x + dx, y + dy, dx, dy)
        # have mainloop repeat this after 100 ms
        root.after(100, self.loop, root)

if __name__ == "__main__":
    root = tkinter.Tk()
    frame = BubbleFrame(root)
    frame.loop(root)
    root.mainloop()