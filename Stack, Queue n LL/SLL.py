#SLL
#SLL Creation, traversing, deletion

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def add_front(self,data):
        node = Node(data)

        if self.head == None:
            #Creating for the first time
            self.head = node
            node.next = None
        else:
            node.next = self.head
            self.head = node
        print(data,' Added at front of list.\n')

    def add_last(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            node.next = None
        else:
            cur = self.head
            while(cur.next != None):
                cur = cur.next

            cur.next = node
            node.next = None
        print(data,' Added at last position.\n')

    def add_index(self, indx, data):
        if indx == 0:
            self.add_front(data)
            print("Added at index 0. i.e Front of list.\n")
            return
        node = Node(data)
        ind = 0
        cur = self.head
        prev = cur
        while True:
            if cur.next == None:
                #last
                self.add_last(data)
                return

            if ind == indx:
                prev.next = node
                node.next = cur
                print(data,' Added at Index: ',ind,'\n')
                return
            ind += 1
            prev = cur
            cur = cur.next


    def print(self):
        if self.head == None:
            print("Empty List\n")
            return
        cur = self.head
        i = 0
        print('Printing List.')
        while cur != None:
            print(i)
            print(cur.data,'\n')
            cur = cur.next
            i+=1
        print('End of list\n')


sll = SLL()
sll.add_front("Asif's list")
sll.add_last([1,2,3,4,5])
sll.add_last((1,2,3,4,5))
sll.add_index(1,98009000010)
sll.add_index(20,800)
sll.print()
sll.add_index(3,["Rador", "Vader", "Ashoka Tano"])
sll.print()


sll.print()