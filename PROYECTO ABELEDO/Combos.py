class Combos:
    def __init__(self, name, products, price):
        self.name = name
        self.products = products
        self.price = price

    
    def __str__(self):
        return f"COMBO\t\t {self.name}\n" \
                f"INCLUYE\t {self.clasification}\n" \
                f"PRECIO \t {self.price}$"