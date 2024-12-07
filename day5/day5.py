import sys


def parse(str_inp):
    parsed_result = str_inp.strip().split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in parsed_result[0].split("\n")]
    order = [list(map(int, order.split(","))) for order in parsed_result[1].split("\n")]

    return rules, order 

rules, orders = parse(open(sys.argv[1]).read())

def populate_rule_map(rules):
    rule_map = {}
    for rule in rules:
        l, r = rule[0], rule[1]
        if l not in rule_map:
            rule_map[l] = []
        rule_map[l].append(r)
    return rule_map

def find_orders(rule_map, orders, correct_orders=True):
    nums_seen_so_far = []
    res_orders = []

    for order in orders:
        for x in order:
            if len(nums_seen_so_far) == 0 or x not in rule_map:
                nums_seen_so_far.append(x)
                continue
            if any(i in nums_seen_so_far for i in rule_map[x]):
                if not correct_orders:
                    res_orders.append(order)
                break
            else:
                nums_seen_so_far.append(x)
        else:
            if correct_orders:
                res_orders.append(order)
        nums_seen_so_far = []
    return res_orders 



def fix_incorrect_orders(rule_map, orders):
    fixed_orders = []
    for order in orders:
        order_fixed = False
        while not order_fixed:
            order_fixed = True
            for i in range(len(order)):
                for j in range(i+1, len(order)):
                    if order[i] in rule_map and order[j] in rule_map[order[i]]:
                        order[i], order[j] = order[j], order[i]
                        order_fixed = False
                        break
                if not order_fixed:
                    break
        fixed_orders.append(order)
    return fixed_orders

def find_mid_point(order):
    return order[len(order) // 2]

def solve(rules, orders):
    rule_map = populate_rule_map(rules)
    correct_orders = find_orders(rule_map, orders)
    p1 = sum(find_mid_point(order) for order in correct_orders)
    incorrect_orders = find_orders(rule_map, orders, False)
    p2 = sum(find_mid_point(order) for order in fix_incorrect_orders(rule_map, incorrect_orders))
    return p1, p2

print(solve(rules, orders))
