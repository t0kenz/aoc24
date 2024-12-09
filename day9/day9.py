import sys

test_input = """2333133121414131402"""

def tester(puzzle):
    p1 = solve(puzzle)
    assert(p1 == 1928)

def parse(puzzle):
    p = list(map(int, puzzle.strip())) 
    blocks, free_blocks = p[::2], p[1::2]
    return blocks, free_blocks

def solve(puzzle):
    blocks, free_blocks = parse(puzzle)
    for id, (block, free_block) in enumerate(zip(blocks, free_blocks)):
        pass

solve(test_input)
