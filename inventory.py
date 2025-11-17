

itemList = {"coke","lucky day","sprite","C2"}
itemsDictionary = {"coke" : 15,
                   "lucky day": 24,
                   "sprite": 15,
                   "C2": 16}

response = 0

while not response == 4:
    try:
        print("INVENTORY MENU")
        print("[1]Add Item")
        print("[2]Update")
        print("[3]Item List")
        print("[4]Exit")
        response = int(input())
        
        if response == 1:
            try:    
                addItem = input("Add Item:")
                if itemsDictionary.get(addItem):
                    print("Item already exist")
                else:
                    addPrice = input(f"Add price to {addItem}:")
                    itemList.add(addItem)
                    itemsDictionary.update({addItem: addPrice})
                    print("Item added successfully!")
            except:
                print("Error in response 1")

        elif response == 2:
            try:
                updateItem = input("What Item do you want to update? ")
                if itemsDictionary.get(updateItem):
                    newPrice = int(input(f"Change price {updateItem} from {itemsDictionary.get(updateItem)} to: "))
                    itemsDictionary[updateItem] = newPrice
                    print("Update Done")
                else:
                    print("Item does not exist")
            except:
                print("Error found in response 2")


        elif response == 3: 
            for key, value in itemsDictionary.items():
                print(f"{key}: {value}")
        elif response == 4:
            break
        else:
            print("Try Again")
    except:
        print("Error in Menu, Please Restart")
print("done")


