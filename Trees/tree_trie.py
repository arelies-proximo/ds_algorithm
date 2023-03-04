#TRIE IMPLEMENTATION

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstring = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                #ch does not exist in current node
                node = TrieNode()
                current.children.update({ch:node})
                #updates(adds) in the dict this value pair
            current = node
        current.endofstring = True
        print('Successfully Inserted.')


    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                #char does not exist
                print('String does not exist.')
                return
            currentNode = node

        #after every char exist in nodes, we check eos
        if currentNode.endofstring == True:
            print('String exist in Trie.')
            return
        else:
            print('String does not exist.')
            return

def deleteString(root, word, index=0):
    #index for the character in the word
    ch = word[index]
    currentNode  = root.children.get(ch)

    canThisNodeBeDeleted = False

    '''this string's prefix is same as other prefix,
    if crntNode children is grtr than one, we can't delete this'''
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
        #to check if thisnodecanbeDeleted variable
    
    #word is prefix of other word
    if index == len(word)-1:
        #index is at the last char
        if len(currentNode.children) >= 1:
            currentNode.endofstring = False
            return False
        else:
            '''since this is the last character, this doesn't hv any
            children node, we pop from dic and return True to 
            delete this node'''
            root.children.pop(ch)
            return True

    #some other word is prefix of to delete word, case 3
    if currentNode.endofstring == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)

    if canThisNodeBeDeleted is True:
        root.children.pop(ch)
        return True
    else:
        return False




newTrie = Trie()
newTrie.insertString('APP')
newTrie.insertString('APPL')
newTrie.searchString('AP')
newTrie.searchString('APPL')
