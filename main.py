import pygame
import sys
from node import Node
from bfs import bfs


pygame.init()

width = 600
rows = 30
cellSize = width // rows

white = (255,255,255)
gray = (200,200,200)

win = pygame.display.set_mode((width,width))
pygame.display.set_caption("2D grid example")

def drawGrid(win,grid,rows,width):
    win.fill(white)

    for row in grid:
        for node in row:
            node.draw(win)
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win,gray,(0,i*gap),(width,i*gap))
        pygame.draw.line(win,gray,(i*gap,0),(i*gap,width))

def makeGrid(rows,width):
    grid = []
    gap = width // rows
    
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,gap,rows)
            grid[i].append(node)
    return grid

def getClickedPos(pos,rows,width):
    gap = width // rows
    x,y = pos
    row = x // gap
    col = y // gap
    return row,col

def main():
    rows = 30
    width = 600
    grid = makeGrid(rows,width)
    start = grid[5][5]
    start.make_start()
    end = grid[10][15]
    end.make_end()
    # Left vertical wall
    grid[4][6].make_barrier()
    grid[5][6].make_barrier()
    grid[6][6].make_barrier()
    grid[7][6].make_barrier()
    grid[8][6].make_barrier()

    # Middle block
    grid[8][7].make_barrier()
    grid[8][8].make_barrier()
    grid[8][9].make_barrier()

# Right vertical wall
    grid[5][12].make_barrier()
    grid[6][12].make_barrier()
    grid[7][12].make_barrier()
    grid[8][12].make_barrier()
    grid[9][12].make_barrier()

# Bottom wall near the end
    grid[10][13].make_barrier()
    grid[10][14].make_barrier()

    
    run = True
    while run:
        drawGrid(win,grid,rows,width)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press space to start BFS
                    for row in grid:
                        for node in row:
                            node.updateNeigbours(grid)

                    bfs(lambda: drawGrid(win, grid, rows, width), grid, start, end)

            
    pygame.quit()
    sys.exit()

main()


