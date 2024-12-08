import sys
import pdb
from collections import defaultdict

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def tester(puzzle):
    p1 = solve1(puzzle)
    print(p1)
    assert(p1 == 14)


def parse(puzzle):
    nodes = defaultdict(list)
    grid = puzzle.strip().splitlines()

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col != '.':
                nodes[col].append((r, c))
    return grid, nodes

def solve1(puzzle):
    seen = set()
    grid, nodes = parse(puzzle)

    for node in nodes:
        n = nodes.get(node)
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                x0, y0 = n[i]
                x1, y1 = n[j]
                dx = abs(x0 - x1)
                dy = abs(y0 - y1)

                new_x = x0 - dx
                new_y = y0 - dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    seen.add((x0 - dx, y0 - dy))


                if (new_x, new_y) == (2, 10):
                    print("hej\n\n\n\n")

                new_x = x1 + dx
                new_y = y1 + dy

                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    seen.add((x1 + dx, y1 + dy))

                if (new_x, new_y) == (2, 10):
                    print("då\n\n\n\n")

    print(seen)
    return len(seen) 

tester(test_input)
