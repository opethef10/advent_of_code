#! /usr/bin/env python
from itertools import cycle

from utils import input_text, input_lines

EMPTY = "."
WALL = "#"
PLAYER = "^"

UP = -1, 0
DOWN = 1, 0
LEFT = 0, -1
RIGHT = 0, +1

DIRECTIONS = cycle([UP, RIGHT, DOWN, LEFT])

def current_position(maze):
    for i, line in enumerate(maze):
        for j, cell in enumerate(line):
            if cell == PLAYER:
                return i, j

def is_in_maze(pos):
    r, c = pos
    if not 0 <= r < width:
        return False
    if not 0 <= c < height:
        return False
    return True

if __name__ == "__main__":
    lines = input_lines(__file__)
    maze = [line.strip() for line in lines]
    height = len(maze)
    width = len(maze[0])

    pos = current_position(maze)
    visited_coords = {pos}

    direction = next(DIRECTIONS)

    while True:
        cr, cc = pos
        mr, mc = direction
        new_pos = (cr + mr), (cc + mc)
        if not is_in_maze(new_pos):
            break

        x, y = new_pos

        if maze[x][y] == WALL:
            direction = next(DIRECTIONS)
        else:
            pos = new_pos
            visited_coords.add(pos)

    print(len(visited_coords))
