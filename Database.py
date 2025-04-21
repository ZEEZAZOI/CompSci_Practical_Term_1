#Warehouse Class
class Warehouse:
    def __init__(self, Xsize, Ysize):
        self.Aisles = Xsize
        self.Rows = Ysize
#Location Class
class Location:
    def __init__(self, Xposition, Yposition):
        self.Xposition = Xposition
        self.Yposition = Yposition
#Product Class
class Product:
    def __init__(self, Name, Quantity, Price):
        self.Name = Name
        self.Quantity = Quantity
        self.Price = Price