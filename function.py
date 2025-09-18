def main():
    age = input("enter age plz ")
    name = input("what ur name ")
    exitchoice = ""
    print("~" * 30)
    def welcome_message(age, name):
        print(f"Welcome {name}, you are {age} years old.")
        print(f"I present you, the Grade calculator!")
        print("~" * 30)

    welcome_message(age, name)
    test_avg = 0
    letter_grade = ""
    while exitchoice != "yes":
        def grade_avg():
            test1 = int(input("what was the score for the first test "))
            test2 = int(input("score for second test "))
            test3 = int(input("what was 3rd test score "))
            test_avg = round((test1 + test2 + test3) / 3, 2)
            print("Your test_avg was ", test_avg)
            if test_avg >= 100:
                test_avg = "A+"
            elif test_avg >= 90:
                test_avg = "A"
            elif test_avg >= 80:
                test_avg = "B"
            elif test_avg >= 70:
                test_avg = "C"
            elif test_avg >= 60:
                test_avg = "D"
            else:
                test_avg = "F"
            print("Letter grade is ", test_avg)

        grade_avg()
        exitchoice = input("leave? ")

main()
