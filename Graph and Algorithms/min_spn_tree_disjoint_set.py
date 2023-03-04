class Disjoint_Set:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        #every vertex as its own parent
        for v in vertices:
            self.parent[v] = v

        self.rank = dict.fromkeys(vertices, 0)  
            #use vertices as keys & val =0 for all vertices
            #rank of all vertices initially is 0
        

    def find_parent(self, item):
        #return parent of set
        #in which set these items are present
        if self.parent[item] == item:
            return item
        else:
            return self.find_parent(self.parent[item])
    
    def union(self, x, y):
        x_root = self.find_parent(x)
        y_root = self.find_parent(y)
        if self.rank[x_root] < self.rank[y_root]:
            #if rank of yroot is greater
            self.parent[x_root] = y_root

        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        
        else:
            #because x comes first in arguement
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
            #the rank can be ZERO or ONE
        

vertices = ['A', 'B', 'C', 'D', 'E']

ds = Disjoint_Set(vertices)



    #=> B  because at beginning item itself is its parent


    # both have zero rank so A will bcom B's parent

    #=> A
'''
ds.union('A', 'B')
print(ds.rank)
print(ds.parent)

print('\n\n')

ds.union('C', 'A')
print(ds.rank)
print(ds.parent)

print('\n\n')

ds.union('D', 'E')
print(ds.rank)
print(ds.parent)

print('\n\n')

ds.union('D', 'B')
print(ds.rank)
print(ds.parent)

'''