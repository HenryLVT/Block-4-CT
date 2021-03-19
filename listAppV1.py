import random
myList = []

def mainProgram():
    print("Hello, there! Let's work with lists!")
    while True:
        try:
            print("Choose one of the following options. Type a number only!")
            choice = input("""1. Add to list,
2. Return the value of an index position
3. Random Search
4. Add a bunch of numbers
5. Print contents of list
6. Do a linear search
7. End program
""")
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                randomSearch()
            elif choice == "4":
                addABunch()
            elif choice == "5":
                print(myList)
            elif choice == "6":
                linearSearch()
                
            else:
                break
        except:
            print("""Hehe hoohoo that wasn't clever
Restarting...""")
                
def addABunch():
        print("We're gonna add a bunch of numbers")
        numToAdd = input("How many intgers do you want to add?   ")
        numRange = input("And how high would you like them to go?")
        for x in range (0,int(numToAdd)):
            myList.append(random.randint(0, int(numRange)))
        print("Your list is now complete")
           
def addToList():
    newItem = input("Please type an integer.")
    myList.append(int(newItem))
    print(myList)

def randomSearch():
    print("Here's a random value from your list")
    print(myList[random.randint(0,len(myList)-1)])
    


def indexValues():
    indexPos = input("Where would you like to look")
    print(myList[int(indexPos)])

def linearSearch():
    print("We're going to search throught the list in the worst way possible")
    searchItem = input("what are you looking for? Number wise")
    amountOfTimes = 0
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            amountOfTimes = amountOfTimes + 1
            print("your item is at index {}".format(x))
    print("Your item is in the list", amountOfTimes,"times")

            

if __name__ == "__main__":
    mainProgram()
