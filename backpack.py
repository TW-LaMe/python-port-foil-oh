exit=""
backpack_items = []
while exit != "exit":
    print("1. Open your backpack")
    print("2. Add an item to your backpack")
    print("3. Remove an item from your backpack")
    print("4. Sort your backpack")
    print("Pop last item from your backpack")
    print("6. Exit")
    exit = input("What would you like to do? (Type 1-6, or exit to quit): ")
    if exit == "1":
        if backpack_items:
            print("\nbackpack contains:\n")
            for item in backpack_items:
                print("-", item)
        else:
            print("\nbackpack is empty.\n")
    elif exit == "2":
        item = input("\nEnter the item you want to add: \n")
        backpack_items.append(item)
        print(f"\n{item} has been added to your backpack.\n")
    elif exit == "3":
        item = input("\nEnter the item you want to remove: \n")
        if item in backpack_items:
            backpack_items.remove(item)
            print(f"\n{item} has been removed from your backpack.\n")
        else:
            print(f"\n{item} is not in backpack.\n")
    elif exit == "4":
        backpack_items.sort()
        print("\nYour backpack has been sorted.\n")
    elif exit == "5": 
        if backpack_items:
            removed_item = backpack_items.pop()
            print(f"\n{removed_item} has been removed from your backpack.\n")
        else:
            print("\nbackpack is empty, nothing to pop.\n")
    elif exit == "6":
        print("\nExiting the backpack program.\n")
    else:
        print("\nInvalid option. Please try again.\n")