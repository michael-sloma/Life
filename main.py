import Tkinter as tk
import random
import algorithm as a
import sys

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Life")
        self.cellsize = 10
        self.ncells = int(args[0])
        self.canvasSize = self.cellsize*self.ncells
        self.canvas = tk.Canvas(self, width=self.canvasSize, height=self.canvasSize, 
                                borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.active = True

        self.rect = {}
        self.oval = {}
        for column in range(self.ncells):
            for row in range(self.ncells):
                x1 = column*self.cellsize
                y1 = row * self.cellsize
                x2 = x1 + self.cellsize
                y2 = y1 + self.cellsize
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2,
                                                                     fill="white", 
                                                                     tags="rect")
                self.canvas.tag_bind(self.rect[row,column], '<ButtonPress-1>', 
                                                        self.switchCell)  
        self.bind('<Return>',self.reset)
        self.bind('<space>',self.toggleActive)
        self.board = a.board(self.ncells,self.ncells)
        self.board.randomize()
        self.redraw(1000)

    def toggleActive(self,event):
        if self.active: self.active = False
        else: self.active = True

    def switchCell(self,event):
        self.board.switch(self.pixToCell(event.x),self.pixToCell(event.y))

    def pixToCell(self,p):
        return (p / self.cellsize)

    def reset(self,event):
        self.board.randomize()

    def redraw(self, delay):
        self.canvas.itemconfig("rect", fill="white")
        for i in range(0,self.ncells):
            for j in range(0,self.ncells):
                if self.board.isAlive(i,j ):
                    item_id = self.rect[i,j]
                    self.canvas.itemconfig(item_id, fill="black")
        if self.active:
            self.board.iterate()
        self.after(delay, lambda: self.redraw(delay))

if __name__ == "__main__":
    usage = "Usage: python main.py <numCells>"
    try:
        if len(sys.argv) > 2: raise IOError
        ncells = sys.argv[1]
        app = App(ncells)
        app.mainloop()
    except (ValueError,IOError):
        print usage
        sys.exit()
