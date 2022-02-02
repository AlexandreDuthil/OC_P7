from decimal import *


class Action:
    def __init__(self, name, price, profits):
        self.name = name
        self.price = int(abs(price)*100)
        with localcontext() as ctx:
            ctx.prec = 2
            self.profits = profits
        with localcontext() as ctx:
            ctx.prec = 6
            self.profitability = Decimal((self.price*self.profits))/10000

    def __eq__(self, compared_object):
        if isinstance(compared_object, Action):
            return self.profits == compared_object.profits
        else:
            raise TypeError("Ne peut pas comparer une Action "
                            "avec un autre type d'objet")

    def __gt__(self, compared_object):
        if isinstance(compared_object, Action):
            return self.profits > compared_object.profits
        else:
            raise TypeError("Ne peut pas comparer une Action "
                            "avec un autre type d'objet")

    def __repr__(self):
        return f"(Name : {self.name}, Price : {self.price}, Profits : {self.profits}," \
               f" Profitability : {self.profitability})"
