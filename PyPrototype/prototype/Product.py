from copy import deepcopy

from .IPrototype import IPrototype

class Product(IPrototype):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def clone(self):
        return Product(self.name, self.price)

    def deep_clone(self):
        return deepcopy(self)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return hex(id(self)) + " - Product{" + \
               "name='" + self.name + '\'' + \
               ", price=" + str(self.price) + \
               '}'
