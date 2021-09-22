from Action import Action

# sans création d'objet, récupération de listes

# def get_action_list(data):
#     names = []
#     prices = []
#     profits = []
#
#     with open(data, "r") as fichier:
#         for line in fichier:
#             if line.find("name") != -1:
#                 continue
#             line = line.replace("\n", "")
#             line = line.split(",")
#             names.append(line[0])
#             prices.append(float(line[1]))
#             profits.append(float(line[2]))
#     return names, prices, profits


# création d'objets Action, POO

def get_action_list(data):
    actions = []
    with open(data, "r") as fichier:
        for line in fichier:
            if line.find("name") != -1:
                continue
            line = line.replace("\n", "")
            line = line.split(",")
            line = Action(line[0], float(line[1]), float(line[2]))
            actions.append(line)
    return actions
