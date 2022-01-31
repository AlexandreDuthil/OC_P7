from itertools import combinations


def brute_force(names, prices, profits, W):
    """
    Brute force algorithm solving knapsack problem
    :param names: names of the actions used as parameters
    :param prices: prices of each actions
    :param profits: profits of each action
    :param W: our wallet, or maximum capacity of knapsack
    :return: best actions set, total profits, total cost
    """
    n = len(names)
    best_actions = None
    best_actions_profits = 0
    final_cost = 0
    for i in range(n):
        print(i)
        for combination in list(combinations(names, i+1)):
            cost = 0
            total_profit = 0
            for element in combination:
                cost += prices[names.index(element)]
                total_profit += (prices[names.index(element)]*profits[names.index(element)])
            if cost <= 500 and total_profit > best_actions_profits:
                best_actions = combination
                best_actions_profits = total_profit
                final_cost = cost
    return best_actions, best_actions_profits/100, final_cost


 # fonctionnement avec POO
def brute_force_POO(actions, W):
    n = len(actions)
    best_actions = []
    best_actions_profits = 0
    final_cost = 0
    for i in range(n):
        for combination in (combinations(actions, i+1)):
            names = []
            cost = 0
            total_profit = 0
            for element in combination:
                cost += element.price
                total_profit += element.profitability
            if cost <= W and total_profit > best_actions_profits:
                for element in combination:
                    names.append(element.name)
                    best_actions = names
                best_actions_profits = total_profit
                final_cost = cost
    return best_actions, best_actions_profits, final_cost
