class Action:
    def __init__(self, name, price, profits):
        self.name = name
        self.price = abs(price)
        self.profits = profits*1/100
        self.profitability = self.price*self.profits

    def __eq__(self, compared_object):
        if isinstance(compared_object, Action):
            return self.profits == compared_object.profits
        else:
            raise TypeError("Ne peut pas comparer une Action avec un autre type d'objet")

    def __gt__(self, compared_object):
        if isinstance(compared_object, Action):
            return self.profits > compared_object.profits
        else:
            raise TypeError("Ne peut pas comparer une Action avec un autre type d'objet")

    def __repr__(self):
        return f"({self.name},{self.price}, {self.profits}, {self.profitability})"