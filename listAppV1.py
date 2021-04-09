import random
import time
myList = []
unique_list = []
lengthIterative = 32

def mainProgram():
    print("Hello, there! Let's work with lists!")
    while True:
        #try:
            print("Choose one of the following options. Type a number only!")
            choice = input("""1. Add to list,
2. Return the value of an index position
3. Random Search
4. Add a bunch of numbers
5. Sort your list
6. Do a linear search
7. Recursive binary search
8. Iterative binary search
9. Print Lists
10. End program
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
                sortList(myList)
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                binSearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                
                binSearch = input("What number are you looking for?   ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1 :
                    print("Your number is at index position {}".format(result))
                    print("Your search took {} seconds".format(lengthIterative))
                else:
                    endIterative = time.time()
                    print("Your number isn't here")
                    print("Your search took {} seconds".format(lengthIterative))
            elif choice == "9":
                printLists()
            
            else:
                break

        #except:

           #print("""Hehe hoohoo that wasn't clever
#Restarting...""")

                
def addABunch():
    startAdding = time.time()
    print("We're gonna add a bunch of numbers")
    numToAdd = input("How many integers do you want to add?   ")
    numRange = input("And how high would you like them to go?")
    for x in range (0,int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    endAdding = time.time()
    print("Your list is now complete")
    print("Your addition took {} seconds to complete".format(endAdding - startAdding))
           
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
    print("We're going to search through the list in the worst way possible")
    searchItem = input("what are you looking for? Number wise")
    amountOfTimes = 0
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            amountOfTimes = amountOfTimes + 1
            print("your item is at index {}".format(x))
    print("Your item is in the list", amountOfTimes,"times")

def recursiveBinarySearch(unique_list, low, high, x):
    startRecursive = time.time()
    if high >= low:
        
        mid = (high + low) // 2
        print("1")

        if unique_list[mid] == x:
            print("Oh what luck your number is at position{}".format(mid))
            endRecursive = time.time()
            print("Your search took {} seconds".format(endRecursive - startRecursive))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low , mid -1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x) 
    else:
        print("Your number isn't here")
        endRecursive = time.time()
        print("Your search took {} seconds".format(endRecursive - startRecursive))

def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("wanna see your new list Y/N")
    if showMe.lower() == "y":
        print(unique_list)

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or un-sorted")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)

def iterativeBinarySearch(unique_list, x):
    #startIterative =  time.time()
    
    low = 0
    high = len(unique_list) - 1
    mid = 0
    print("this happened")
    while low <= high:
        mid = (high + low) //2
        print("this two")

        if unique_list[mid] < x:
            low = mid + 1
            lengthIterative = endIterative - startIterative
            print(" this one")

        elif unique_list[mid] > x:
            high = mid -1
            print(" this thing happened")
            lengthIterative = endIterative - startIterative

        else:
            return mid
            lengthIterative = endIterative - startIterative
    return -1
    endIterative = time.time()
    lengthIterative = endIterative - startIterative
if __name__ == "__main__":
    mainProgram()
