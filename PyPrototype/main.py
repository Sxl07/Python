from prototype.PriceList import PriceList
from prototype.Product import Product

def main():
    # Lista de precios inicial
    price_list = PriceList("Lista normal")
    product_list = [
        Product("Computadora", 650000),
        Product("Mouse", 120000),
        Product("Teclado", 80000),
        Product("Pantalla", 1350000),
        Product("Auriculares", 40000)
    ]
    price_list.set_product_list(product_list)

    print(price_list)
    print()

    # Segunda lista de precios con descuento
    price_list2 = price_list.clone()
    price_list2.set_name("Lista Prefer")

    for product in price_list2.get_product_list():
        product.set_price(product.get_price() * 0.9)

    print(price_list2)
    print()

    # Tercera lista de precios con descuento
    price_list3 = price_list.clone()
    price_list3.set_name("Lista VIP")

    for product in price_list3.get_product_list():
        product.set_price(product.get_price() * 0.5)

    print(price_list3)
    print()

if __name__ == "__main__":
    main()
