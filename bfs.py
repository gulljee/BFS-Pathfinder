from queue import Queue
from node import Node

def bfs(draw, grid, start, end):
    queue = Queue()
    queue.put(start)
    visited = {start}

    while not queue.empty():
        draw()

        current = queue.get()

        if current == end:
            reconstruct_path(current, draw)
            end.make_end()
            return True

        for neighbour in current.neighbours:
            if neighbour not in visited and not neighbour.isBarrier():
                visited.add(neighbour)
                neighbour.previous = current
                queue.put(neighbour)
                neighbour.make_open()

        if current != start:
            current.make_closed()

    return False
def reconstruct_path(current, draw):
    while current.previous:
        current = current.previous
        if current.previous:
            current.make_path()
        draw()