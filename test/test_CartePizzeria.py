import CartePizzeria
import pytest
def test_is_empty():
    carte = CartePizzeria.CartePizzeria()
    with pytest.raises(Exception):
        carte.is_empty()
def test_nb_pizzas():
    carte = CartePizzeria.CartePizzeria()
    with pytest.raises(Exception):
        carte.nb_pizzas()
def test_add_pizza():
    carte = CartePizzeria.CartePizzeria()
    with pytest.raises(Exception):
        carte.add_pizza()
def test_remove_pizza():
    carte = CartePizzeria.CartePizzeria()
    with pytest.raises(Exception):
        carte.remove_pizza()