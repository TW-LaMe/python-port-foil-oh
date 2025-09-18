#tip toucher.py
import os
bill = float(input("tell me the total chaching deducted amount: "))
tip_percentage = float(input("what is the extra chaching percentage (e.g., 15 for 15%): "))
tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("extra chaching amount: {:.2f}".format(tip_amount))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("total amount of chaching to be deducted: {:.2f}".format(total_amount))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("THANK YOU FOR USING THIS PROGRAM!")
print("AND GET OUT!")

clear = input("Press Enter to clear the screen.")
os.system('cls' if os.name == 'nt' else 'clear')
print("Screen cleared. Goodbye!")