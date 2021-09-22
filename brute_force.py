from itertools import combinations


def brute_force(n, actions, wallet):
    leafs = []
    for i in range(n):
        for j in list(combinations(actions, i+1)):
            print(j)
