import numpy as n
import random
class board:
    def __init__(self,x,y,randomize=True):
        self.xdim = x
        self.ydim = y
        self.offset = 1
        self.board = n.zeros((x+2,y+2),dtype=int)
        if randomize: self.randomize()


    def randomize(self):
        for i in range(1,self.xdim):
            for j in range(1,self.ydim):
                self.board[i][j]=random.randint(0,1)

    def numNeighbors(self,x,y):
        return sum([self.board[a][b] for a in range(x-1,x+2) 
                                     for b in range(y-1,y+2)
                                     if not (a==x and b==y)])

    def rule(self,x,y):
        neighbors = self.numNeighbors(x,y)
        if neighbors==3: return 1
        elif neighbors==2: return self.board[x][y]
        else: return 0

    def iterate(self):
        nextBoard = n.zeros((self.xdim+2,self.ydim+2),dtype=int)
        for x in range(1,self.xdim):
            for y in range(1,self.ydim):
                nextBoard[x][y] = self.rule(x,y)
        self.board = nextBoard

    def isAlive(self,i,j):
        if i>self.xdim or j>self.ydim: return 0
        if i<self.offset or j<self.offset: return 0
        return self.board[i+self.offset][j+self.offset]

    def switch(self,j,i):
        i+=1
        j+=1 #correct for offset
        if (self.xdim > i > 0) and (self.ydim > j > 0):
            current = self.board[i][j]
            if current==1: self.board[i][j] = 0
            elif current==0: self.board[i][j] = 1
            else: raise AssertionError