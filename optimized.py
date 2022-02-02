from Node import Node


def optimized(actions, W):
    """
       Optimized algorithm solving knapsack problem with dynamic programming
       :param actions: list of Actions objects
       :param W: our wallet, or maximum capacity of knapsack
       :return: best_actions, best_actions_profits, final_cost
    """
    W = W*100
    n = len(actions)
    mat = [[0 for x in range(W + 1)] for x in range(n + 1)]
    action_list = []
    result = 0
    cost = 0

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif actions[i - 1].price < j:
                mat[i][j] = max(actions[i - 1].profitability +
                                mat[i - 1][j - actions[i - 1].price],
                                mat[i - 1][j])
            else:
                mat[i][j] = mat[i - 1][j]

    r = mat[n][W]
    while r != 0:
        if mat[n - 1][W] == r:
            n -= 1
        else:
            r = mat[n - 1][W - actions[n - 1].price]
            W -= actions[n - 1].price
            n -= 1
            action_list.append(actions[n])
            result += actions[n].profitability
    for action in action_list:
        cost += action.price
    cost = cost/100

    return action_list, result, cost


def optimized_POO(actions, W):
    n = len(actions)
    W = W*100
    mat = [[Node() for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                pass
            elif actions[i - 1].price < j:
                if (actions[i - 1].profitability +
                    mat[i - 1][j - actions[i - 1].price].value) > mat[i - 1][
                        j].value:
                    mat[i][j].add_action(actions[i - 1])
                    mat[i][j].add_action(
                        mat[i - 1][j - actions[i - 1].price].action_list)
                else:
                    mat[i][j] = mat[i - 1][j]
            else:
                mat[i][j] = mat[i - 1][j]

    return mat[n][W]
