from file_reader import get_action_list
from brute_force import brute_force
from optimized import optimized
import time

start = time.time()
data = "data/dataset2_Python+P7.csv"
# names, prices, profits = get_action_list(data) #  fonctionnement sans objet Action
actions = get_action_list(data) #  fonctionnement avec POO
W = 500


# best_actions, total_profits, final_cost = brute_force(names, prices, profits, W) #  fonctionnement sans objet Action
# best_actions, total_profits, final_cost  = brute_force(actions, W) #  fonctionnement avec POO

# print(best_actions, total_profits, final_cost, resolve_time)

print(optimized(actions, W*100)/100)
stop = time.time()
print(stop - start)

#TODO : tester optimized sans la POO, comparer la rapidité
#TODO : réorganiser les algo POO/pasPOO, ça devient fouilli