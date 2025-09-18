password=""

while password != "supercoolpassword":
    password = input("Enter the password: ")
    if password == "supercoolpassword":
        print("Access granted! Welcome back.")
    else:
        print("Access denied. Try again.")

