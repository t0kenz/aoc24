import sys
from collections import defaultdict
from math import gcd

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
    p1 = solve(puzzle)
    p2 = solve(puzzle, True)
    print(p1, p2)
    assert(p1 == 14 and p2 == 34)

def parse(puzzle):
    nodes = defaultdict(list)
    grid = puzzle.strip().splitlines()

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col != '.':
                nodes[col].append((r, c))
    return grid, nodes

def solve(puzzle, p2=False):
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

                if p2:
                    # https://stackoverflow.com/questions/26392324/normalize-a-vector-differently-than-normal thanks stackoverflow <3
                    step_size = gcd(dx, dy)
                    dx //= step_size
                    dy //= step_size

                    # input size is 50x50
                    for k in range(-50, 50):
                        x3, y3 = x0 + k * dx, y0 + k * dy
                        if 0 <= x3 < len(grid) and 0 <= y3 < len(grid[0]):
                            seen.add((x3, y3))

    return len(seen)

tester(test_input)
print(solve(open(sys.argv[1]).read(), True))
