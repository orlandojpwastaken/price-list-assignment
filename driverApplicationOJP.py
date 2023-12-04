from classModuleOJP import FoodItemOJP
def createListOJP():
    itemList = []

    amountItems = int(input("Enter the amount of different items: "))

    while amountItems < 1:
        print("You must enter at least one item.")
        amountItems = int(input("Enter the amount of different items: "))
    else:
        for i in range (amountItems):
            nameItem = input(f"Please insert the name of Item {i+1}: ")
            amountPounds = float(input(f"Insert the amount of pounds for this item: "))
            while amountPounds < 0:
                print ("You have entered a negative value. Please enter again.")
                amountPounds = float(input(f"Insert the amount of pounds for this item: "))
            foodAdd = FoodItemOJP(nameItem, amountPounds)
            itemList.append(foodAdd)
    return itemList
        
def displayListOJP(foodList):
    print("Here is a list of all the items purchased:")
    print("------------------------------------------")
    for food in foodList:
        print(f"{food.getNameOJP()}")
        print(f"Amount: {food.getPoundsOJP()}")
        print(f"Total Cost: {food.getTotalPriceOJP()}")
        print("-----------------------------------------")

def mainOJP():
    myFoodList = createListOJP()

    displayListOJP(myFoodList)

mainOJP()
    

