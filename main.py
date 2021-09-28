##this file will act as a menu for the user to select which part of my program to go to
import calculator
import realator
print("Please Select:")
print("1: I'm a new real estate agent.")
print("2: I need a mortgage calculator.")
number = int(input())
if number == 1:
    realator.intro()
    realator.randomize()
elif number == 2:
    calculator.writeFile(calculator.person)
else:
    print("Invalid Input")
