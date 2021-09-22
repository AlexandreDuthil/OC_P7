from file_reader import get_action_list
from brute_force import brute_force
import time

start = time.time()
data = "data/dataset0_Python+P7.csv"
names, prices, profits = get_action_list(data) #  fonctionnement sans objet Action
# actions = get_action_list(data) #  fonctionnement avec POO
W = 500


best_actions, total_profits, final_cost = brute_force(names, prices, profits, W) #  fonctionnement sans objet Action
# best_actions, total_profits, final_cost  = brute_force(actions, W) #  fonctionnement avec POO
stop = time.time()

resolve_time = stop - start

print(best_actions, total_profits, final_cost, resolve_time)

