import random
def intro():
    print("Welcome new realators!")
    print("Selecting a place to start your practice is tough!")
    print("This program will help you select a random place!")

##for loop to get places, add them to the list
def function_1():
    places = []
    print("Please enter 5 places you are considering:")
    for x in range(5):
        place = input("Enter Place:")
        places.append(place)
    number = random.randint(0, 4)
    print("Your randomized location is: " + places[number])

    
    
