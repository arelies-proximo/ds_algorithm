import queue

class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrderTraversal(node):
    if not node:
        # if link = None
        return
    print(node.data)
    # call left nodes recursively
    preOrderTraversal(node.left)
    # call right nodes after left one
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if not node:
        return
    # if a node is None
    inOrderTraversal(node.left)
    print(node.data)
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    # check if node exist
    if not node:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data)


def levelOrderTraversal(node):
    if not node:
        return
    else:
        customq = queue.Queue()
        customq.enqueue(node)
        while not(customq.isEmpty()):
            root = customq.dequeue()
            print(root.data)
            if root.left is not None:
                customq.enqueue(root.left)
            if root.right is not None:
                customq.enqueue(root.right)


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "Binary tree does not exist"
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not customq.isEmpty():
            root = customq.dequeue()
            if root.data == nodeValue:
                return f"Success,{nodeValue} Node exist in Binary Tree."
            if root.left is not None:
                customq.enqueue(root.left)
            if root.right is not None:
                customq.enqueue(root.right)

        # if value is not in BT
        return f"{nodeValue} does not exist in BT"


def insertNodeBT(rootNode, newNode):
    if not rootNode:
        # root not doesn't exist
        rootNode  = newNode
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not customq.isEmpty():
            root = customq.dequeue()
            if root.left is not None:
                customq.enqueue(root.left)
            else:
                # left is empty => assign new node
                root.left = newNode
                print('Successfully inserted.')
                return
            if root.right is not None:
                customq.enqueue(root.right)
            else:
                # right is empty => assign new node
                root.right = newNode
                print('Successfully inserted.')
                return

def getDeepestNode(rootNode):
    if not rootNode:
        print("Tree doesn't exist")
        return
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not customq.isEmpty():
            root = customq.dequeue()

            if root.left is not None:
                customq.enqueue(root.left)

            if root.right is not None:
                customq.enqueue(root.right)
        deepestNode = root
        return deepestNode


def deleteDeepestNode(rootNode):
    """dNode = deepest node"""
    dNode = getDeepestNode(rootNode)
    if not rootNode:
        print("Tree doesn't exist!")
        return
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not customq.isEmpty():
            root = customq.dequeue()
            if root is dNode:
                print(f"{root.data}(last Node) deleted from Binary tree.")
                root = None
                return
            if root.right:
                # if r8 node present, check if it is the node or else enq
                if root.right is dNode:
                    print(f"{root.right.data}(Last Node) deleted from Binary tree.")
                    root.right = None
                    return
                else:
                    customq.enqueue(root.right)

            if root.left:
                if root.left is dNode:
                    print(f"{root.left.data}(Last Node) deleted from Binary tree.")
                    root.left = None
                    return
                else:
                    customq.enqueue(root.left)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        print('BT does not exist')
        return
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not customq.isEmpty():
            root = customq.dequeue()
            if root.data == nodeValue:
                dNode = getDeepestNode(rootNode)
                root.data = dNode.data
                deleteDeepestNode(rootNode)
                print(nodeValue,'\'s Node deleted.')
                return
            if root.left is not None:
                customq.enqueue(root.left)
            if root.right is not None:
                customq.enqueue(root.right)
        print('Failed to delete Node.')
        return


def deleteBinaryTree(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    print("Binary tree has been successfully deleted.")


drink = BTNode('Drinks')
hot = BTNode('Hot')
cold = BTNode('Cold')
drink.left = hot
drink.right = cold
tea = BTNode('Tea')
hot.left = tea
coffee = BTNode('Coffee')
hot.right = coffee



deleteBinaryTree(drink)

preOrderTraversal(drink)