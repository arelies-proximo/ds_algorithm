"""Binary Tree using Fixed length List"""


class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastIndexUsed = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastIndexUsed + 1 == self.maxSize:
            print("The Binary tree is full")

        self.customList[self.lastIndexUsed + 1] = value
        self.lastIndexUsed += 1
        print(value, " value has been inserted.")

    def searchNode(self, nodeValue):
        for i in range(self.lastIndexUsed + 1):
            if self.customList[i] == nodeValue:
                print('Success, Node exist in Binary Tree.')
                return
        print("Node not found.")

    def preOrderTraversal(self, index=1):
        if index > self.lastIndexUsed:
            return
        print(self.customList[index], end=' -> ')
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index=1):
        if index > self.lastIndexUsed:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index], end=' -> ')
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index=1):
        if index > self.lastIndexUsed:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        if index == 1:
            # root node will be printed last
            print(self.customList[index])
            return
        print(self.customList[index], end=' -> ')

    def levelOrderTraversal(self, index=1):
        # in list items are inserted in level order only
        if self.lastIndexUsed == 0:
            print('Binary Tree does not exit.')
            return
        for i in range(index, self.lastIndexUsed + 1):
            if i == self.lastIndexUsed:
                print(self.customList[i])
                return
            print(self.customList[i], end=' -> ')

    def deleteNode(self, value):
        if self.lastIndexUsed == 0:
            print('Tree not present.')
            return
        for i in range(1, self.lastIndexUsed + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastIndexUsed]
                self.customList[self.lastIndexUsed] = None
                self.lastIndexUsed -= 1
                print(value, ' Node has been deleted.')
                return

    def deleteBinaryTree(self):
        prompt = input('Delete Binary Tree (y/n): ').lower()
        if prompt == 'y':
            self.customList = None
            self.lastIndexUsed = 0
            print("Binary Tree has been deleted.")
            return



new_binary_tree = BinaryTree(10)

new_binary_tree.insertNode('Drinks')
new_binary_tree.insertNode('Hot')
new_binary_tree.insertNode('Cold')
new_binary_tree.insertNode('Tea')
new_binary_tree.insertNode('Coffee')

new_binary_tree.postOrderTraversal()
new_binary_tree.levelOrderTraversal()
new_binary_tree.deleteNode('Cold')
new_binary_tree.levelOrderTraversal()


new_binary_tree.deleteBinaryTree()
new_binary_tree.levelOrderTraversal()