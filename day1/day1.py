import sys
from collections import Counter

puzzle_path = sys.argv[1]
puzzle_input = [x.split() for x in open(puzzle_path).read().split("\n")]

l = []
r = []
for v in puzzle_input:
    l.append(int(v[0]))
    r.append(int(v[1]))

p1 = sum(abs(x - y) for x, y in zip(sorted(l), sorted(r)))

occurrences = Counter(r)
p2 = sum(x * occurrences[x] for x in l)

print(f"p1: {p1}, p2: {p2}")