class Restaurant:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name   


restaurant = Restaurant("KFC")
restaurant1 = Restaurant("Movenpick")

print(restaurant1.name())

