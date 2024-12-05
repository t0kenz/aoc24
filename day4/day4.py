import sys
from enum import Enum

puzzle_input = open(sys.argv[1]).read().splitlines()

class Directions(Enum):
    NORTH     = (-1, 0)
    SOUTH     = (1, 0)
    EAST      = (0, 1)
    WEST      = (0, -1)
    NORTHEAST = (-1, 1)
    NORTHWEST = (-1, -1)
    SOUTHWEST = (1, -1)
    SOUTHEAST = (1, 1)

xmas_dirs = [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST, Directions.NORTHEAST, Directions.NORTHWEST, Directions.SOUTHWEST, Directions.SOUTHEAST]
mas_dirs = [Directions.SOUTHEAST, Directions.SOUTHWEST]

def part1():
    to_find = "XMAS"
    tot = 0
    for row in range(len(puzzle_input)):
        for col in range(len(puzzle_input[0])):
            if puzzle_input[row][col] != 'X':
                continue
            for direction in xmas_dirs:
                for i in range(4):
                    x, y = direction.value
                    dx = row + x * i
                    dy = col + y * i
                    if 0 <= dx < len(puzzle_input) and 0 <= dy < len(puzzle_input[0]):
                        if puzzle_input[dx][dy] != to_find[i]:
                            break
                    else:
                        break
                else:
                    tot += 1
    return tot


def part2():
    to_find = "MAS"
    tot = 0
    for row in range(len(puzzle_input)):
        for col in range(len(puzzle_input[0])):
            if puzzle_input[row][col] == 'M' or puzzle_input[row][col] == 'S':
                found = 0
                for dir in mas_dirs:
                    if dir == Directions.SOUTHEAST:
                        c = 0
                    else:
                        c = 2
                    for seq in ["MAS", "SAM"]:
                        for i in range(3):
                            x, y = dir.value
                            dx = row + x * i
                            dy = col + c + y * i

                            if 0 <= dx < len(puzzle_input) and 0 <= dy < len(puzzle_input[0]):
                                if puzzle_input[dx][dy] != seq[i]:
                                    break
                            else:
                                break
                        else:
                            found += 1
                if found == 2:
                    tot += 1
    return tot

print(part1())
print(part2())

