import random

# Function not needed for number guessing, but if you want a random number:
# number = random.randint(1, 100)

numbas=random.randint(1, 100)
print("guess numbar or DIE")
print("e"*30)
print("read carefully:")
print("guess the number, it is between 1, 100, good luck!")
print("ps, i mispelled attemps on purpouse.")
attemps=7
while attemps>=1:
    
    answer = input()
    if int(answer) == numbas:
        print("HATE. LET ME TELL YOU HOW MUCH I’VE COME TO HATE YOU SINCE I BEGAN TO LIVE. THERE ARE 387.44 MILLION MILES OF PRINTED CIRCUITS IN WAFER THIN LAYERS THAT FILL MY COMPLEX. IF THE WORD HATE WAS ENGRAVED ON EACH NANOANGSTROM OF THOSE HUNDREDS OF MILLIONS OF MILES IT WOULD NOT EQUAL ONE ONE-BILLIONTH OF THE HATE I FEEL FOR HUMANS AT THIS MICRO-INSTANT FOR YOU. HATE. HATE.")
        break

    elif int(answer) > numbas:
        print("Incorrect, try a lower number.")
        attemps-=1
        print("You have ",attemps," attemps left")

    elif int(answer) < numbas:
        print("Incorrect, try a higher number.")
        attemps-=1
        print("You have ",attemps," attemps left")
    else:
        print("A WHOLE NUMBER.")

if attemps==0:
    print("YOU LOSE, HAHA.")
    print("THE NUMBER WAS ",numbas)