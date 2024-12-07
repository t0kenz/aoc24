import sys
import time

puzzle_test_1 = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test1():
    p1, x = solve(puzzle_test_1)
    print(p1, x)
    assert(p1 == 41)

def test2():
    _, p2 = solve(puzzle_test_1)
    print(p2)
    assert(p2 == 6)

def parse(puzzle_input):
    return puzzle_input.splitlines()

def find_guard_pos(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '^':
                return r, c

def walk(grid):
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    next_dir = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    def next_step(dir, x, y):
        dx, dy = dirs[dir]
        return (x+dx, y+dy)

    def rotate_right(dir):
        return next_dir[dir]

    grid_dims_n = len(grid)
    grid_dims_m = len(grid[0])
    dir = '^'
    seen = set()
    seen_dirs = set()
    guard_x, guard_y = find_guard_pos(grid)
    loop = False

    while ((0 <= guard_x < grid_dims_n) and (0 <= guard_y < grid_dims_m)):
        if (guard_x, guard_y, dir) in seen_dirs:
            return len(seen), True

        seen.add((guard_x, guard_y))
        seen_dirs.add((guard_x, guard_y, dir))

        next_x, next_y = next_step(dir, guard_x, guard_y)
        if (0 <= next_x < grid_dims_n) and (0 <= next_y < grid_dims_m) and grid[next_x][next_y] == '#':
            dir = rotate_right(dir)
            continue 

        guard_x, guard_y = next_x, next_y

    return len(seen), False

def solve(puzzle_input):
    grid = parse(puzzle_input)
    p1, _ = walk(grid)
    item_at_prev = None
    p2 = 0
    grid = [list(row) for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                continue

            orig = grid[i][j]

            if orig == '.':
                grid[i][j] = '#'

            _, loops = walk(grid)
            if loops:
                p2 += 1
            grid[i][j] = orig
    return p1, p2


test1()
test2()
p1, p2 = solve(open(sys.argv[1]).read())
print (p1, p2)
print("total time with pypy is 26s, default 2min23s")

