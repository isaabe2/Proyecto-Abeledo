class Cruceros:
    def __init__(self, name, route, departure, cost, rooms, capacity ):
        self.name = name
        self.route = route
        self.departure = departure
        self.cost= cost
        self.rooms = rooms
        self.capacity = capacity

    

    
    def __str__(self):
        return f"NOMBRE\t\t {self.name}\n" \
               f"DESTINOS\t {self.route}\n" \
               f"FECHA\t\t {self.departure}\n"\
               f"PRECIOS: \t HAB. SIMPLE: {self.cost['simple']}\n \t\t HAB. PREMIUM:{self.cost['premium']}\n \t\t HAB. VIP: {self.cost['vip']}\n " \
               f"HAB. PASILLO:\t SIMPLE: {self.rooms['simple'][0]} pasillos, {self.rooms['simple'][1]} habitaciones\n \t\t PREMIUM: {self.rooms['premium'][0]} pasillos, {self.rooms['premium'][1]} habitaciones\n \t\t VIP:{self.rooms['vip'][0]} pasillos, {self.rooms['vip'][1]}\n" \
               f"CAPACIDAD:\t SIMPLE: {self.capacity['simple']}\n \t\t PREMIUM: {self.capacity['premium']}\n \t\t VIP: {self.capacity['vip']}\n" \

    def get_route(self):
        return self.route

    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity
    
    
    