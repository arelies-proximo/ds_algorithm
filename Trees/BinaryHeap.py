# BINARY HEAP IMPLEMENTATION

class Heap:
    def __init__(self, size, type='max'):
        self.customList = (size+1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1
        if type.lower() == 'min':
            self.heaptype = 'min'
        else:
            self.heaptype = 'max'


def peek(rootNode):
    #returns the root node data of the tree
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapsize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapsize+1):
            print(rootNode.customList[i])

def heapify(rootNode, index):
    heapType = rootNode.heaptype
    #index is where the item is inserted, we check it parents
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            #parent must be lesser
            #swap
            rootNode.customList[index],rootNode.customList[parentIndex] = rootNode.customList[parentIndex],rootNode.customList[index]

        #we call heapify to check for the parent Node
        heapify(rootNode, parentIndex)
    elif heapType == "max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            #parent must be greater
            #swap
            rootNode.customList[index],rootNode.customList[parentIndex] = rootNode.customList[parentIndex],rootNode.customList[index]

        #we call heapify to check for the parent Node
        heapify(rootNode, parentIndex)

def insertNode(rootNode, nodeValue):
    if rootNode.heapsize+1 == rootNode.maxsize:
        return "B Heap is full"
    rootNode.customList[rootNode.heapsize+1] = nodeValue
    rootNode.heapsize += 1
    heapify(rootNode, rootNode.heapsize)


def heapifyTreeExtract(rootNode, index):
    heaptype = rootNode.heaptype
    leftIndex = index *2
    rightIndex = index*2 + 1
    swapChild = 0

    if rootNode.heapsize < leftIndex:
        #there are no node present above heapsize
        #rootNode has no child
        return
    elif rootNode.heapsize == leftIndex:
        #only one child for current NOde
        if heaptype == 'min':
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                #swap
                tmp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = tmp
            return
        else:
            #max heap
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                #swap
                tmp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = tmp
            return

    else:
        '''if node has two children, swap with greater/smllr child'''

        if heaptype == 'min':
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                '''left child is smaller or not'''
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.custmoList[swapChild]:
                '''if root is grtr thn swapchild, swap it'''
                rootNode.custmoList[swapChild],rootNode.customList[index] = rootNode.customList[index],rootNode.custmoList[swapChild]

        else:
            '''maximum heap, replace with max child'''
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                '''left child is grtr or not'''
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChild]:
                '''if root is smlr thn swapchild, swap it'''
                rootNode.customList[swapChild],rootNode.customList[index] = rootNode.customList[index],rootNode.customList[swapChild]
    #if swapchild occurs we recurs it with swpchild index
    heapifyTreeExtract(rootNode, swapChild)

def extractNode(rootNode):
    if rootNode.heapsize == 0:
        return
    else:
        extrctNode  = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapsize]
        rootNode.heapsize -= 1

        heapifyTreeExtract(rootNode, 1)
        return extrctNode


def deleteEntireTree(rootNode):
    rootNode.customList = None

new_heap = Heap(5, 'max')

insertNode(new_heap, 4)
insertNode(new_heap, 5)
insertNode(new_heap, 2)
insertNode(new_heap, 1)

print(extractNode(new_heap), end='\n\n\n')
levelOrderTraversal(new_heap)
