from copy import deepcopy

from .IPrototype import IPrototype

class PriceList(IPrototype):
    def __init__(self, name):
        self.name = name
        self.product_list = []

    def clone(self):
        clone = PriceList(self.name)
        clone.product_list = self.product_list[:]  # Shallow copy the list
        return clone

    def deep_clone(self):
        clone = PriceList(self.name)
        clone.product_list = [product.clone() for product in self.product_list]  # Deep copy each product
        return clone

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_product_list(self):
        return self.product_list

    def set_product_list(self, product_list):
        self.product_list = product_list

    def __str__(self):
        product_list_str = "[" + ", ".join(str(product) for product in self.product_list) + "]"
        return hex(id(self)) + " - PriceList{" + \
               "name='" + self.name + '\'' + \
               ", productList=" + product_list_str + \
               '}'
