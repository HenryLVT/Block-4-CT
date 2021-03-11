import random
myList = []

def mainProgram():
    while True:
        print("Hello, there! Let's work with lists!")
        print("Choose one of the following options. Type a number only!")
        choice = input("""1. Add to list,
2. Return the value of an index position
3. End program
4.Random Search""")
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues
        elif choice == "3":
            break
        elif choice == "4":
            randomSearch


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

if __name__ == "__main__":
    mainProgram()
