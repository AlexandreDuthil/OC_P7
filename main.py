from file_reader import get_action_list
from brute_force import brute_force

data = "data/dataset1_Python+P7.csv"
actions = get_action_list(data)

brute_force(len(actions), actions, 500)