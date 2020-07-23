from Cruceros import Cruceros
class Rooms:
    def __init__(self, clase, capacity,cost, hallway, hab):
        self.clase = clase
        self.capacity = capacity
        self.cost = cost
        self.hallway = hallway
        self.hab = hab
        

    def __str__(self):
        return f"CLASE\t\t {self.clase}\n" \
                f"PRECIO\t\t {self.cost}$\n" \
                f"CAPACIDAD \t {self.capacity} personas\n"\
                

    def get_capacity(self):
        return self.capacity

    def get_hallway(self):
        return self.hallway

    def get_hab(self):
        return self.hab
    
    def get_cost(self):
        return self.cost

    def get_class(self):
        return self.clase
