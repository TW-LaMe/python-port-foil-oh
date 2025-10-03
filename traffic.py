import random
import os

# Smart Traffic Light System
# DO NOT use max(), sorted(), or any built-in sorting methods.
# Use ONLY if-elif-else statements for all logic.

# Use this Input structure
densities = ["Low", "Medium", "High"]

traffic = {
    "North": {"density": random.choice(densities), "emergency": random.choice([True, False])},
    "South": {"density": random.choice(densities), "emergency": random.choice([True, False])},
    "East": {"density": random.choice(densities), "emergency": random.choice([True, False])},
    "West": {"density": random.choice(densities), "emergency": random.choice([True, False])}
}
print("Traffic Status:"+str(traffic)+"\n")

def density_to_the_number(density):
    if density == "Low":
        return 1
    elif density == "Medium":
        return 2
    elif density == "High":
        return 3
    else:
        return 0
    
def traffic_light_system(traffic):
    if traffic["North"]["emergency"] == True and traffic["North"]["density"] == "High":
        print("North NOW")
    elif traffic["South"]["emergency"] == True and traffic["South"]["density"] == "High":
        print("South NOW")
    elif traffic["East"]["emergency"] == True and traffic["East"]["density"] == "High":
        print("East NOW")
    elif traffic["West"]["emergency"] == True and traffic["West"]["density"] == "High":
        print("West NOW")
    elif traffic["North"]["emergency"] == True and traffic["North"]["density"] == "Medium":
        print("North Quickly")
    elif traffic["South"]["emergency"] == True and traffic["South"]["density"] == "Medium":
        print("South Quickly")
    elif traffic["East"]["emergency"] == True and traffic["East"]["density"] == "Medium":
        print("East Quickly")
    elif traffic["West"]["emergency"] == True and traffic["West"]["density"] == "Medium":
        print("West Quickly")
    elif traffic["North"]["emergency"] == True and traffic["North"]["density"] == "Low":
        print("North, hurry up")
    elif traffic["South"]["emergency"] == True and traffic["South"]["density"] == "Low":
        print("South, hurry up")
    elif traffic["East"]["emergency"] == True and traffic["East"]["density"] == "Low":
        print("East, hurry up")
    elif traffic["West"]["emergency"] == True and traffic["West"]["density"] == "Low":
        print("West, hurry up")
    elif traffic["North"]["density"] == "High":
        print("Release pressure on North")
    elif traffic["South"]["density"] == "High":
        print("Release pressure on South")
    elif traffic["East"]["density"] == "High":
        print("Release pressure on East")
    elif traffic["West"]["density"] == "High":
        print("Release pressure on West")
    elif traffic["North"]["density"] == "Medium":
        print("Let North go")
    elif traffic["South"]["density"] == "Medium":
        print("Let South go")
    elif traffic["East"]["density"] == "Medium":
        print("Let East go")
    elif traffic["West"]["density"] == "Medium":
        print("Let West go")
    elif traffic["North"]["density"] == "Low":
        print("North can go")
    elif traffic["South"]["density"] == "Low":
        print("South can go")
    elif traffic["East"]["density"] == "Low":
        print("East can go")
    elif traffic["West"]["density"] == "Low":
        print("West can go")
    else:
        print("Woah, all directions are clear!")


traffic_light_system(traffic)
clear_screen = input("Do you want to clear the screen? (yes/no): ").strip().lower()
if clear_screen == 'yes':
    os.system('cls' if os.name == 'nt' else 'clear')
else:
    print("Fine, have it your way.")
