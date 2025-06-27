import pygame
class Node:
    def __init__(self,row,col,width,totalRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.color = (255,255,255)
        self.totalRows = totalRows
        self.neighbours = []
        self.previous = None
    
    def getPos(self):
        return self.row,self.col
    def isClosed(self):
        return self.color == (255,0,0)
    def isOpen(self):
        return self.color == (0,255,0)
    def isBarrier(self):
        return self.color == (0,0,0)
    def reset(self):
        self.color = (255,255,255)
    def make_start(self):
        self.color = (255, 165, 0)  

    def make_closed(self):
        self.color = (255, 0, 0)  

    def make_open(self):
        self.color = (0, 255, 0)  

    def make_barrier(self):
        self.color = (0, 0, 0)
    def make_end(self):
        self.color = (0, 0, 255)
    def make_path(self):
        self.color = (255, 255, 0)
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
    def updateNeigbours(self, grid):
        self.neighbours = []
        row = self.row
        col = self.col

        # Down
        if row < self.totalRows - 1 and not grid[row + 1][col].isBarrier():
            self.neighbours.append(grid[row + 1][col])

        # Up
        if row > 0 and not grid[row - 1][col].isBarrier():
            self.neighbours.append(grid[row - 1][col])

        # Right
        if col < self.totalRows - 1 and not grid[row][col + 1].isBarrier():
            self.neighbours.append(grid[row][col + 1])

        # Left
        if col > 0 and not grid[row][col - 1].isBarrier():
            self.neighbours.append(grid[row][col - 1])
