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

    for node, positions in nodes.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x0, y0 = positions[i]
                x1, y1 = positions[j]

                dx, dy = x1 - x0, y1 - y0

                antinode1 = (x0 - dx, y0 - dy)
                if 0 <= antinode1[0] < len(grid) and 0 <= antinode1[1] < len(grid[0]):
                    seen.add(antinode1)

                antinode2 = (x1 + dx, y1 + dy)
                if 0 <= antinode2[0] < len(grid) and 0 <= antinode2[1] < len(grid[0]):
                    seen.add(antinode2)
    return len(seen) 

def solve2(puzzle):

tester(test_input)
print(solve1(open("input.txt").read()))
