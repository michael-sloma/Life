import Tkinter as tk
import random
import algorithm as a

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Life")
        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellwidth = 25
        self.cellheight = 25

        self.rect = {}
        self.oval = {}
        for column in range(20):
            for row in range(20):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")
                #self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="white", tags="oval")
        self.bind('<Return>',self.reset)
        self.board = a.board(20,20)
        self.board.randomize()
        self.redraw(1000)

    def reset(self,event):
        self.board.randomize()

    def redraw(self, delay):
        self.canvas.itemconfig("rect", fill="white")
        for i in range(0,19):
            for j in range(0,19):
                if self.board.isAlive(i,j ):
                    item_id = self.rect[i,j]
                    self.canvas.itemconfig(item_id, fill="black")
        self.board.iterate()
        self.after(delay, lambda: self.redraw(delay))

if __name__ == "__main__":
    app = App()
    app.mainloop()
