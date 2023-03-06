
class CartePizzeria:
    def __init__(self):
        self.__pizzas = []

    def is_empty(self):
        return len(self) == 0

    def nb_pizzas(self):
        return len(self)

    def add_pizza(self, pizza):
        for p in self.__pizzas:
            if p.name == pizza.name:
                raise Exception("CartePizzeriaException")
            return False
        self.__pizzas.append(pizza)

    def remove_pizza(self, pizza):
        for p in self.__pizzas:
            if p.name == pizza:
                self.__pizzas.remove(p)
                return True
        raise Exception("CartePizzeriaException")
