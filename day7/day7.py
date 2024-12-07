import sys
from itertools import product
import math

test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def tester():
    p1, p2 = solve(test)
    assert(p1 == 3749 and p2 == 11387)

def parse(puzzle):
    res = [x.split(":") for x in puzzle.splitlines()]
    res = [(int(x[0]), list(map(int, x[1].strip().split(" ")))) for x in res]
    return res

def eval_exprs(terms, ops, p2):
    res = terms[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            res += terms[i + 1]
        elif ops[i] == '*':
            res *= terms[i + 1]
        elif p2 and ops[i] == '||':
            # this is slower hehe (inspiration from reddit)
            #res = res * pow(10, math.ceil(math.log(terms[i+1], 10))) + terms[i+1]
            res = int(str(res) + str(terms[i + 1]))

    return res 

def find_ops(lhs, rhs, p2=False):
    operators = ['+', '*', '||'] if p2 else ['+', '*']
    for ops in product(operators, repeat=len(rhs)-1):
        res = eval_exprs(rhs, ops, p2)
        if res == lhs:
            return True
    return False

def solve(puzzle):
    p = parse(puzzle)
    p1 = sum(x for x, y in p if find_ops(x,y))
    p2 = sum(x for x, y in p if find_ops(x, y, True))
    return p1, p2


tester()
print(solve(open(sys.argv[1]).read()))
