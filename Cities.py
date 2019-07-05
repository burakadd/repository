class City(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Transport(object):
    def __init__(self, basicvelocity, relativecost):
        self.basicvelocity = basicvelocity
        self.relativecost = relativecost

    @abstractmethod
    def travel(self, destination, ):
        pass


class Plane(Transport):













_dict = [{"name": "Megapolis", x: 20, y: 20}, {"name": "City", x: -15, y: 15}, {
    "name": "Town", x: 5, y: -5}, {"name": "Village", x: 0, y: 0}]