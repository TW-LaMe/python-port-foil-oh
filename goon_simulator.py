import math
people=input("Enter the number of people: ")
people=float(people)
chaching=input("Enter the amount of chaching each person has: ")
chaching=float(chaching)
chaching_cost=input("Enter the amount of chaching deducted: ")
chaching_cost=float(chaching_cost)
def calculate_chaching(people, chaching, chaching_cost):
    total_chaching = people * chaching
    total_chaching -= chaching_cost
    return total_chaching
print("Total chaching after deduction: ", calculate_chaching(people, chaching, chaching_cost))