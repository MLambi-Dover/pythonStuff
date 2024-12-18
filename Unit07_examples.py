# Unit 07
# Problem 1: Count of Digits (12 points)
print("Problem 1: Count of Digits\n")
# Create a list with 1000 random numbers valued 0-9.
# Count the frequency of the different numbers.

from random import randint
myList = []

# We will create a list of random numbers of a fixed length.
for number in range(1000):       # We can use a for loop to step through the range
    myList.append(randint(0,9))  # and add each new number to the end of the list
                                 # using the list-method append.
for number in range(10):         # We will use a static range to count from 0 to 9.
    # Then we use the built-in list-method to count unique items in the list.
    print(f'There are {myList.count(number)} of the number {number}')
print()

# Problem 2: Smallest Index (12 points)
# Required function: def indexOfSmallesElements(lst):
# returns minIndex
# Write a function that takes a list as a parameter.
# The function will search the list and return the index of the
# smallest number.
# Create a list of 15 numbers valued 0-100.
# Output the random list and then the value of the smallest number
# and the index.
# Do NOT use sor(), max() or min() functions.
print('\nProblem 2: Smallest Index')

myList.clear()  # might as well reuse the list from before.

for i in range(15):
    myList.append(randint(0,100))

print("The contents of the list are:\n", myList)

lowestNumberIndex = 0
lowestNumberValue = 100
currentIndexValue = 0
for item in myList:
    if item < lowestNumberValue:
        lowestNumberValue = item
        lowestNumberIndex = currentIndexValue
    currentIndexValue += 1

print(f'The smallest number is {lowestNumberValue} at index {lowestNumberIndex}\n')
# or, even better; don't need either of the Index variables.
print(f'The smalles number is {lowestNumberValue} at the index {myList.index(lowestNumberValue)}\n')

# Problem 3: List Shuffle (12 points)
print("Problem 3: List Shuffle")
# Required function heading - def shuffle(lst): returns shuffled list
# First, generate a list of 10 random numbers from 0-100.
# Print the unsortes list, then sort the list and print the sorted version.
# Then pass the list to the shuffle function and print the results.
myList.clear()  # reusing the same old list...  Make sure it is empty.
for i in range(10):
    myList.append(randint(0,100))

print(f"The initial list is:        {myList}")

myList.sort()
print(f'The sorted list is:         {myList}')

def shuffle(lst):  # returns the list shuffled
    newList = []
    listValue = None
    while lst:
        listValue = lst.pop(randint(0,len(myList)-1))
        newList.append(listValue)
    return newList

myList = shuffle(myList)
print(f'The newly shuffled list is: {myList}\n')

# Problem 4: Revise Selection Sort (14 points)
# Required function heading - def selectionSortsm(lst):
# Required function heading - def selectionSortlg(lst):
print("Problem #4")

def selectionSortsm(lst):
  swaps = 0  #swaps counts how many times numbers were swapped to get the list in order
  for i in range(len(lst)):
    # Find the minimum in the lst[i : len(lst)]
    currentMin = lst[i]
    currentMinIndex = i
    
    #looks to see if there is a smaller number in the list and sets that to the smallest if it finds it
    for j in range(i + 1, len(lst)):
      if currentMin > lst[j]:
        currentMin = lst[j]
        currentMinIndex = j
    
    # Swap lst[i] with lst[currentMinIndex] if necessary
    if currentMinIndex != i:
      lst[currentMinIndex] = lst[i]
      lst[i] = currentMin
      swaps += 1
  print("Swaps", swaps)

#create a list and sort with function
myList.clear()
for i in range(20):
  myList.append(randint(0,100))

myListCopy = myList.copy()  #  make a copy for the second sort
print(f'The initial list is:  {myListCopy}')
selectionSortsm(myListCopy)
print(f'The sorted list is:  {myListCopy}')
print()

def selectionSortlg(lst):
  swaps = 0  #swaps counts how many times numbers were swapped to get the list in order
  for i in range(len(lst)-1, 0, -1):
    # Find the minimum in the lst[i : len(lst)]
    currentMax = lst[i]
    currentMaxIndex = i
    
    #looks to see if there is a smaller number in the list and sets that to the smallest if it finds it
    for j in range(i - 1, -1, -1):
      if currentMax < lst[j]:
        currentMax = lst[j]
        currentMaxIndex = j
    
    # Swap lst[i] with lst[currentMinIndex] if necessary
    if currentMaxIndex != i:
      lst[currentMaxIndex] = lst[i]
      lst[i] = currentMax
      swaps += 1
  print("Swaps", swaps)

myListCopy = myList.copy()  # refresh the list
print(f'Sort lg')
print(f'The unsorted list:  {myListCopy}')
selectionSortlg(myListCopy)
print(f'The sorted list is: {myListCopy}')
print()



print("Problem 5: Bubble Sort (12 points)")
# create a list of 10 random numbers from 0-100
myList.clear()
myList = [randint(0,100) for x in range(10)]
print(f'The original list is:               {myList}')

def bubbleSort(lst):
    swaps = 0
    sorted = False

    while not sorted:
        swapped = False
        for i in range(len(lst) -1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swaps += 1
                swapped = True
        if swapped == False:
           sorted = True

    return lst, swaps
   
lst, swaps = bubbleSort(myList)
print(f'There were {swaps} swaps.')
print(f'The results of the bubble sort are: {myList}\n')
print()
print(f"Problem 6: Merge Sort (14 points)")

def merge(lst1, lst2):
    running = True
    resultinglist = []
    while lst1 or lst2:
        if lst1 and lst2:
            if lst1[0] < lst2[0]:
                resultinglist.append(lst1.pop(0))
            else:
                resultinglist.append(lst2.pop(0))
        elif lst1:
            resultinglist.append(lst1.pop(0))
        elif lst2:
            resultinglist.append(lst2.pop(0))
        else:
           print('an impassible situation occurred')

    return resultinglist

list1 = [randint(0,100) for x in range(10)]
list2 = [randint(0,100) for x in range(10)]
print(f"list1 is: {list1}\nlist2 is: {list2}\n")
list1.sort()
list2.sort()
print(f"list1 is:  {list1}\nlist2 is:  {list2}\n")
print(f"The merged list is:\n{merge(list1, list2)}\n")


print(f"Problem 7: Locker Problem (12 points)")
lockerList = [False for i in range(101)]  # This is the list of 100 lockers;
                                          # they all start off false/closed.
for studentNumber in range(1, 101):       # This represents each student as they go in.

    for studentStep in range(studentNumber, 101, studentNumber):  # This is the 'step' each student takes.
        if lockerList[studentStep]:
            lockerList[studentStep] = False
        else:
           lockerList[studentStep] = True

for item in range(101):
   if lockerList[item]:
      print(f"Locker {item} is open.")
