#stack implementation



class Stack:
    def __init__(self):
        #initializer, constructer
        self.list  = []

    def __str__(self):
        #inorder to print a instance of stack

        values = [str(x) for x in self.list]
        return 'Stack Elements\n' + '\n'.join(values)
    #isempty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #push at top
    def push(self,item):
        self.list.insert(0,item)
        print(f"{item} inserted at top successfully.\n")
        return

    def pop(self):
        if self.isEmpty():
            print("Sorry the Stack is empty")
            return
        print(self.list.pop(0),' popped from the stack.\n')

    def insert_n_items(self):
        n = int(input('Enter num of item to push to stack: '))
        print('Enter ',n,' items seperated by space.')
        vals = input().split()
        for i in vals:
            i = int(i)
            self.push(i)
        print(n,' item inserted')


st = Stack()
st.pop()
st.push(10)
print(st)
st.insert_n_items()
print(st)
for i in range(3):
    st.pop()
