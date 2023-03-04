import queue


class avl_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    # traversal copied from bst
    def preOrderTraversal(self, rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraversal(rootNode.left)
        self.preOrderTraversal(rootNode.right)

    def inOrderTraversal(self, rootNode):
        if not rootNode:
            return
        self.inOrderTraversal(rootNode.left)
        print(rootNode.data)
        self.inOrderTraversal(rootNode.right)

    def postOrderTraversal(self, rootNode):
        if not rootNode:
            return
        self.postOrderTraversal(rootNode.left)
        self.postOrderTraversal(rootNode.right)
        print(rootNode.data)

    def levelOrderTraversal(self, rootNode):
        if not rootNode:
            return
        else:
            customq = queue.Queue()
            customq.enqueue(rootNode)
            while not customq.isEmpty():
                root = customq.dequeue()
                print(root.data)
                if root.left:
                    customq.enqueue(root.left)
                if root.right:
                    customq.enqueue(root.right)


def searchNode(rootNode, value):
    if rootNode.data == value:
        print('Node exist in Binary Search Tree')
        return
    if value < rootNode.data:
        searchNode(rootNode.left, value)
    else:
        searchNode(rootNode.right, value)


def getHeight( rootNode ):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.left

    disbalancedNode.left = disbalancedNode.left.right

    newRoot.right = disbalancedNode

    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.right), getHeight(disbalancedNode.left))
    newRoot.height = 1 + max(getHeight(newRoot.right), getHeight(newRoot.left))
    return newRoot


def leftRotate(disbalncedNode):
    newRoot = disbalncedNode.right
    disbalncedNode.right = disbalncedNode.right.left
    newRoot.left = disbalncedNode
    disbalncedNode.height = 1 + max(getHeight(disbalncedNode.right), getHeight(disbalncedNode.left))
    newRoot.height = 1 + max(getHeight(newRoot.right), getHeight(newRoot.left))
    return newRoot


def checkBalanced(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left) - getHeight(rootNode.right)
    #if grtr thn 1, left condition; less thn 0, right cndtn


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return avl_node(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.left = insertNode(rootNode.left, nodeValue)
    else:
        rootNode.right = insertNode(rootNode.right, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.right), getHeight(rootNode.left))
    balance = checkBalanced(rootNode)

    if balance >1 and nodeValue < rootNode.left.data:
        # left left condition
        return rightRotate(rootNode)
    if balance >1 and nodeValue > rootNode.left.data:
        # left right condition (leftR to root.left)
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)

    if balance < -1 and nodeValue > rootNode.right.data:
        # right right => leftRot
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.left.data:
        # right left: rightR to root.right
        rootNode.right = rightRotate(rootNode.right)
        return leftRotate(rootNode)

    return rootNode


def get_successor(rootNode):
    # the above node is the right child of to be deleted node
    if rootNode is None or rootNode.left is None:
        return rootNode
    return get_successor(rootNode.left)  # .left coz there is min val


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)
    else:
        #nodeVal == root.data
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        elif rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp

        #two child
        temp = get_successor(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)

    #check rotation

    balance = checkBalanced(rootNode)
    if balance > 1 and checkBalanced(rootNode.left) >= 0:
        #left left condition
        return rightRotate(rootNode)
    if balance > 1 and checkBalanced(rootNode.left) < 0:
        #left right
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance < -1 and checkBalanced(rootNode.right) <= 0:
        return leftRotate(rootNode)
    if balance < -1 and checkBalanced(rootNode.right) > 0:
        rootNode.right = rightRotate(rootNode.right)
        return leftRotate(rootNode)
    return rootNode





new_avl = avl_node(5)
new_avl = insertNode(new_avl, 10)
new_avl = insertNode(new_avl, 15)
new_avl = insertNode(new_avl, 20)

new_avl.levelOrderTraversal(new_avl)
new_avl = deleteNode(new_avl, 20)
new_avl.levelOrderTraversal(new_avl)

