from Action import Action


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
