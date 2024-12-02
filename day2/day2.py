import sys

puzzle_levels = [map(int, x.split(" ")) for x in open(sys.argv[1]).read().splitlines()]

is_safe_adjacent = lambda lst: not(any(abs(x-y) < 1 or abs(x-y) > 3 for x, y in zip(lst, lst[1:])))
is_safe_incr_decr = lambda lst: not(any(x > y for x, y in zip(lst, lst[1:]))) or not(any(x < y for x, y in zip(lst, lst[1:])))
is_safe = lambda lst: is_safe_adjacent(lst) and is_safe_incr_decr(lst)
is_safe_after_removal = lambda lst: any(is_safe(lst[:i] + lst[i+1:]) for i in range(len(lst)))

p1 = sum(1 for x in puzzle_levels if is_safe(x))
p2 = sum(1 for x in puzzle_levels if is_safe(x) or is_safe_after_removal(x))
print(p1, p2)