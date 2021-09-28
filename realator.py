import random
##This function will just display a simple explanation of this program
def intro():
    print("Welcome new realators!")
    print("Selecting a place to start your practice is tough!")
    print("This program will help you select a random place!")

## this function will use a for loop to get 5 places and put them in a list
## it will then pick a random place from the list and diplay it to the user
def randomize():
    places = []
    print("Please enter 5 places you are considering:")
    for x in range(5):
        place = input("Enter Place:")
        places.append(place)
    number = random.randint(0, 4)
    print("Your randomized location is: " + places[number])

    
    
