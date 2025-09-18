day="monday"
if day == "Saturday" or day == "Sunday":
    print(f"today is {day}")
    print("It's the weekend!")
    print("Time to relax!")
else:
    print(f"today is {day}")
    print("It's a weekday.")
    print("Time to work, \x1B[3magain.\x1B[0m")