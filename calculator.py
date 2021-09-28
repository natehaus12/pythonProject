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
    payment = (((loan_rate/100)/12) * loan_amount) / (1 - (1 +(loan_rate/100)/12) ** (loan_time * -12))
    print("Your monthly loan payment would be:")
    print(round(payment, 2))
    return (round(payment, 2))

##this will determine which category they fall into and display places they can live
def readFile():
    payment = calculate()
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
## lets make a class for the person, make a list for each payment section, need to implement loop
def writeFile():
    payment = readFile()
    string = str(payment)

    info = open("info.txt", "a")
    print("Would you like to send your information to agents in these areas?")
    decision = input("Enter 1 for YES. Enter 2 for NO. ")
    if decision == "1":
        name = input("Please Enter your first and last name: ")
        info.write("Name: " + name + " | " + "Expected Mortagage: " + string + "\n")
    else:
        print("Thank you for using my program.")
 ##real estate menu, can see file, see the list,



        
        



##calculate() ## 5.25, 10, 100,000
##readFile()
##writeFile()