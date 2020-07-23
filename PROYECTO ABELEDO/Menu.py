class Platos:
    def __init__(self, name, clasification, price):
        self.name = name
        self.clasification = clasification
        self.price = price

    
    def __str__(self):
        return f"PLATO\t\t {self.name}\n" \
                f"CLASIFICACION\t {self.clasification}\n" \
                f"PRECIO \t {self.price}$"

    def change_name(self,name):
        self.name = change_name
        return name

    def change_clasification(self,clasification):
        self.clasification = clasification
        return clasification

    def change_price(self,price):
        self.price = price
        return price
             
    def get_name(self):
        return self.name

    