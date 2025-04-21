#Warehouse Class
class Warehouse:
    def __init__(self, Xsize, Ysize):
        self.Aisles = Xsize
        self.Rows = Ysize
    def Display(self):
    #Making it into a 2D array
        TableArray = []
        for j in range(self.Rows):
            TableArray.append()
            for i in range(self.Aisles):
                TableArray[j](" X ")
        #Displaying it using a print Statement
        for j in range(len(TableArray[j])):
            print(TableArray[j])
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
# First Make the Warehouse Size and display
warehouse1 = Warehouse(10,10)
print(warehouse1.Rows)
