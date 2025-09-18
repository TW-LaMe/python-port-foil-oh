foods=["pizza", "burger", "pasta", "salad"]
print("Welcome to the food ordering system! Here are your options:", foods)

new_food=input("Please enter a new food item to add to the menu: ")
foods.append(new_food)
print("Updated menu:", foods)


remove_food=input("Please enter a food item to remove from the menu: ")
if remove_food in foods:
    foods.remove(remove_food)
    print("Updated menu after removal:", foods)
else:
    print("Did you mispell the food item? It was not found in the menu.")
print("Current menu:", foods)
print("Total items in the menu:", len(foods))
should_sort=input("Would you like to sort the menu? (yes/no): ").strip().lower()
if should_sort == "yes":
    foods.sort()
    print("Sorted menu:", foods)
else:
    print("Menu remains unsorted:", foods)
print("Thank you for using the food ordering system! Goodbye!")