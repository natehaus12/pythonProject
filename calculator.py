## this function will get the variables needed to calculate the monthly mortgage
def get_info():
    print("Welcome to the home mortgage calculator.")
    print("This program will calculate your monthly payment on a loan for a house.")
    print("It will aslo display different places you can afford to live based on the average mortgage of a studio apartment in that area.")
    print("Lets start by getting your information!")
    loan_amount = float(input("Please Enter Your Loan Amount: "))
    loan_time = float(input("Please Enter the Length of Your Loan in Years: "))
    loan_rate = float(input("Please Enter the Interest Rate of Your Loan: "))
    return loan_amount, loan_time, loan_rate


## this function will actually caculate and print the mortgage
def calculate():
    loan_amount, loan_time, loan_rate = get_info()
    if loan_amount <= 0 or loan_time <= 0 or loan_rate <= 0 or loan_rate >= 100:
        print("Invalid Input")
        return 0
    else:
        payment = (((loan_rate/100)/12) * loan_amount) / (1 - (1 +(loan_rate/100)/12) ** (loan_time * -12))
        print("Your monthly loan payment would be:")
        print(round(payment, 2))
        return (round(payment, 2))



##this will determine which category they fall into and display places they can live from a file
def readFile():
    payment = calculate()
    if payment > 0: 
        print("Based on your monthly payment, you could afford the average house in:")
        high = open("high.txt" ,"r")
        mid = open("mid.txt", "r")
        low = open("low.txt", "r")
        if payment < 2500:
            print(low.read())
            return payment
        elif payment >= 2500 and payment <= 3700:
            print(mid.read())
            return payment
        elif payment > 3700:
            print(high.read())
            return payment
    else:
        return 0

## lets make a class for the person to store all their info in the same place
class person:
    name = " "
    adress = " "
    email = " "
    gender = " "
    mortgage = " "

## this function will ask the user if they want to send their information to real estate agents. 
## If they select yes it will ask for their info/ put it into a class and write it to a file
## This file could hypothetically be sent to real estate agents
def writeFile(person):

    payment = readFile()
    if payment != 0:
        person.mortgage = str(payment)

        info = open("info.txt", "a")
        print("Would you like to send your information to agents in these areas?")
        decision = input("Enter 1 for YES. Enter 2 for NO. ")
        if decision == "1":
            person.name = input("Please Enter your first and last name: ")
            person.address = input("Current adress:")
            person.email = input("Email:")
            person.gender = input("Gender:")
            info.write("Name: " + person.name + " | " + "Expected Mortagage: " + person.mortgage +  " | " + "Adress: " + person.address + " | " + "Email: " + person.email + " | " + "Gender: " + person.gender + "\n")
            print("Thank you! These agents may contact you soon.")
        else:
            print("Thank you for using my program.")

        
