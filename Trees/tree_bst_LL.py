"""Binary Search Tree using Linked List"""
import queue
#queue for levelOrder traversal

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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


def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = BSTNode(nodeValue)
        else:
            insertNode(rootNode.left, nodeValue)
    else:
        if rootNode.right is None:
            rootNode.right = BSTNode(nodeValue)
        else:
            insertNode(rootNode.right, nodeValue)
    return "Node has been inserted"


def searchNode(rootNode, value):
    if rootNode.data == value:
        print('Node exist in Binary Search Tree')
        return
    if value < rootNode.data:
        searchNode(rootNode.left, value)
    else:
        searchNode(rootNode.right, value)

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)
    else:
        #   rootNode.data == nodeValue
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp

        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp

        #if node has two children

        temp = minimumValueRightofNode(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    return rootNode


def minimumValueRightofNode(btsNode):
    # to find the min value from this node(this is right side of the
    # required tree node
    current = btsNode
    while current.left is not None:
        # min value are located at left part
        current = current.left
    return current


def deleteBinaryTree(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None

    print('Entire Binary Tree has been deleted.')



new_search_tree = BSTNode(None)
insertNode(new_search_tree, 70)
insertNode(new_search_tree, 50)
insertNode(new_search_tree, 90)
insertNode(new_search_tree, 30)
insertNode(new_search_tree, 20)
insertNode(new_search_tree, 40)
insertNode(new_search_tree, 60)
insertNode(new_search_tree, 80)
insertNode(new_search_tree, 100)


deleteNode(new_search_tree, 70)
new_search_tree.levelOrderTraversal(new_search_tree)

deleteBinaryTree(new_search_tree)




