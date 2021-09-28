import calculator
import realator
print("Please Select:")
print("1: I'm a new real estate agent.")
print("2: I need a mortgage calculator.")
number = int(input())
if number == 1:
    realator.intro()
    realator.function_1()
elif number == 2:
    calculator.writeFile()
