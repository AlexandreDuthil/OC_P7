from file_reader import get_action_list, get_action_list_POO
from brute_force import brute_force, brute_force_POO
from optimized import optimized
import time

data = "data/dataset0_Python+P7.csv"
W = 500

start = time.time()
names, prices, profits = get_action_list(data)  # fonctionnement sans objet Action
best_actions, total_profits, final_cost = brute_force(names, prices, profits, W)  # fonctionnement sans objet Action
stop = time.time()

start_POO = time.time()
actions = get_action_list_POO(data)  # fonctionnement avec POO
best_actions_POO, total_profits_POO, final_cost_POO = brute_force_POO(actions, W)  # fonctionnement avec POO
stop_POO = time.time()



print(F"Sans POO : \n"
      F"Meilleures actions : {best_actions}\n"
      F"Gains totaux : {total_profits}\n"
      F"Prix final : {final_cost}\n"
      F"Running time : {(stop-start)}\n")

print(F"Avec POO : \n"
      F"Meilleures actions : {best_actions_POO}\n"
      F"Gains totaux : {total_profits_POO}\n"
      F"Prix final : {final_cost_POO}\n"
      F"Running time : {(stop_POO-start_POO)}\n")

# print(optimized(actions, W*100)/100)
# stop = time.time()
# print(stop - start)

#TODO : tester optimized sans la POO, comparer la rapidité
#TODO : réorganiser les algo POO/pasPOO, ça devient fouilli