#SORTING ALGORITHM
import math
from typing import ValuesView

def bubbleSort(customList):
    for i in range(len(customList) -1):
        swap_flag = False
        for j in range(len(customList) -1):
            if customList[j] < customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
                swap_flag = True
        #if no swap occurs 
        if swap_flag is False:
            break
    print(customList)


def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            #find min item in rest of list, update pos of min item
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j>=0 and key < customList[j]:
            #move the key to the left to its position
            customList[j+1] = customList[j]
            j -= 1
            
        customList[j+1] = key
    print(customList)


def bucketSort(customList):
    num_buckets = round(math.sqrt(len(customList)))

    max_val = max(customList)
    arr = []

    for i in range(num_buckets):
        arr.append([])
    
    for item in customList:
        index_buk = math.ceil(item*num_buckets/max_val)
        arr[index_buk - 1].append(item)
    
    for i in range(num_buckets):
        arr[i] = sorted(arr[i])
    
    new_list = []
    for i in range(num_buckets):
        for j in range(len(arr[i])):
            new_list.append(arr[i][j])
    
    print(new_list)




def merge(customList, start, mid, end):
    num1 = mid - start + 1
    num2 = end - mid

    left_arr = customList[start:mid+1]
    right_arr = customList[mid+1:end+1]
    
    k = start
    i = 0
    j = 0
    while i < num1 and j < num2:
        if left_arr[i] <= right_arr[j]:
            customList[k] = left_arr[i]
            i += 1
        else:
            customList[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < num1:
        customList[k] = left_arr[i]
        i += 1
        k += 1 
    while j < num2:
        customList[k] = right_arr[j]
        j += 1
        k += 1



def mergeSort(customList, start, end):
    if start<end:
        mid = (start + (end-1)) //2
        mergeSort(customList, start, mid)
        mergeSort(customList, mid+1, end)
        merge(customList, start, mid, end)
    return customList


def partition(customList, low, high):
    #choose pivot, place less item to its left and grtr at its right
    #low is strtng index
    i = low - 1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    #exchng bigger val with pivot 
    customList[i+1], customList[high] = customList[high], customList[i+1]

    #return the pivot's index
    return i+1


def quickSort(customList, low, high):
    if low < high:
        piv_index = partition(customList, low, high)
        quickSort(customList, low, piv_index-1)
        quickSort(customList, piv_index, high)



#HEAP SORT

def heapify(customList, size, index):
    smallest_index = index
    left = 2*index + 1
    right = 2*index + 2

    #smallest child
    if left<size and customList[left]< customList[smallest_index]:
        smallest_index = left
    
    if right<size and customList[right]< customList[smallest_index]:
        smallest_index = right
    
    if smallest_index != index:
        #swap with smaller child
        customList[index], customList[smallest_index] = customList[smallest_index], customList[index]

        #call heapify for child subtree from where we swapped
        heapify(customList, size, smallest_index)
    

def heapSort(customList):
    size = len(customList)

    for i in (range(int(size/2)-1, -1, -1)):
        #building heap tree, from size/2-1
        #in complete bin tree, all parent nodes are before size/2-1
        heapify(customList, size, i)
    
    #extracting element
    for i in range(size-1, 0, -1):
        '''start from i = lastindex
        swap it with first(smallst) node
        => smallest is now placed at  last
        last index at first, heapify => smlst will come at root(ind=0) again
        i = lastIndex-1
            continue the same process, put the smallest node at the end and apply heapyfiy to
            the reduced array
        '''
        
        customList[i], customList[0]= customList[0], customList[i]
        print(customList)
        heapify(customList, i, 0)
    #last is the smallest, then second last smaller and so on....
    #10,9,8 => descending order
    customList.reverse()
    




new_list = [2, 1, 7, 5, 3, 4, 9, 8]

heapSort(new_list)
print(new_list)


