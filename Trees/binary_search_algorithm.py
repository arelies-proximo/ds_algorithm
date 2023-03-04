#SEARCH ALGORITHMS
import random

#LINEAR/SEQUENTIAL

def linearSearch(customList, value):
    for i in range(len(customList)):
        if customList[i]== value:
            print(f"{value} found at index {i}.\n")
            return
    print(value, 'not found!\n')


def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = (start+end)//2      #floor division

    while not(array[middle]== value) and start<=end:
        if value < array[middle]:
            end = middle-1
        else:
            start = middle + 1
            #we already checked middle val
        middle = (start+end)//2 
    
    if array[middle] == value:
        print(f"{value} found at index {middle}.\n")
    else:
        print('404\nValue not Found!')
    
    

new_list = [i for i in range(20)]

print(new_list)

binarySearch(new_list, 9)


