from Action import Action


class Node:
    def __init__(self):
        self.action_list = []
        self.value = 0

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        elif isinstance(other, float):
            return self.value == other
        else:
            raise TypeError("cannot compare to none Int or Float type")

    def __gt__(self, other):
        if isinstance(other, int):
            return self.value > other
        elif isinstance(other, float):
            return self.value > other
        else:
            raise TypeError("cannot compare to none Int or Float type")

    def __repr__(self):
        return f"({self.value})"

    def add_action(self, action):
        if isinstance(action, Action):
            self.action_list.append(action)
            self.value += action.profitability
        elif isinstance(action, list):
            for x in action:
                if isinstance(x, Action):
                    self.add_action(x)
                else:
                    raise TypeError("cannot add none Action type 2")
        else:
            raise TypeError("cannot add none Action type")
