#Warehouse Class
class Warehouse:
    def __init__(self, Xsize, Ysize):
        self.Aisles = Xsize
        self.Rows = Ysize
    def Display(self):
    #Making it into a 2D array
        TableArray = []
        for j in range(self.Rows):
            TableArray.append([])
            for i in range(self.Aisles):
                TableArray[j].append('X')
        #Displaying it using a print Statement
        for j in range(len(TableArray)):
            if j == 0:
                print("TABLE VIEW:")
            else:
                print("row " + str(j))
            for i in range(len(TableArray[j])):
                if i == 0:
                    print("| " + str(TableArray[j][i]), end=" | ") #Making sure to put a separating line at the start
                else:
                    print(TableArray[j][i], end=" | ")
        print("row",len(TableArray))
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
warehouse1 = Warehouse(3,2)
warehouse1.Display()
