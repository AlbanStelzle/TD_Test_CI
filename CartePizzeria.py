class CartePizzeria:
    def __init__(self):
        self.__pizzas = []

    def is_empty(self):
        return len(self) == 0

    def nb_pizzas(self):
        return len(self)

    def add_pizza(self, pizza):
        self.__pizzas.append(pizza)

    def remove_pizza(self, pizza):
        if pizza not in self.__pizzas:
            raise Exception("CartePizzeriaException")
        else:
            self.__pizzas.remove(pizza)
