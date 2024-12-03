import sys
import re

puzzle_input = open(sys.argv[1]).read()
p = re.compile(r"mul\((\d+),(\d+)\)")
p1 = sum(int(x) * int(y) for x, y in p.findall(puzzle_input))

text = "do()" + puzzle_input + "don't()"
index = 0
muls = []

# blä
while True:
    do = text.find("do()", index)
    dont = text.find("don't()", index)

    if do != -1 and dont != -1:
        strsplice = text[do + 4: dont]
        muls.append(strsplice)
        index = dont + len("don't()")
    else:
        break

p2 = sum(int(x) * int(y) for block in muls for x, y in p.findall(block))
print(p1, p2)
