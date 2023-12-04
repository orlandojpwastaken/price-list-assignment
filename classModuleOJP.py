class FoodItemOJP:
    def __init__(self, name, amountInPounds):
        self.__name = name
        self.__amountInPounds = amountInPounds
        self.__unitPrice = 0
        self.__totalPrice = self.getTotalPriceOJP()
        self.__PriceListOJP()
        

    def __PriceListOJP(self):
        if self.__name == "Dry Cured Iberian Ham":
            self.__unitPrice = 177.80

        elif self.__name == "Wagyu Steaks":
            self.__unitPrice = 450.00

        elif self.__name == "Matsutake Mushroooms":
            self.__unitPrice = 272.00

        elif self.__name == "Kopi Luwak Coffee":
            self.__unitPrice = 487.20
        
        elif self.__name == "Moose Cheese":
            self.__unitPrice = 487.20

        elif self.__name == "White Truffles":
            self.__unitPrice = 3600.00

        elif self.__name == "Blue Fin Tuna":
            self.__unitPrice = 3603.00

        elif self.__name == "Le Bonnotte Potatoes":
            self.__unitPrice = 270.81

        else:
            self.__unitPrice = 0 

    def getTotalPriceOJP(self):
        self.__totalPrice = self.__unitPrice * self.__amountInPounds
        return self.__totalPrice
    
    def getNameOJP(self):
        return self.__name
    
    def getPoundsOJP(self):
        return self.__amountInPounds
    
    def __str__(self):
        return f"{self.__amountInPounds} Pounds of {self.__name} = {self.__totalPrice}"