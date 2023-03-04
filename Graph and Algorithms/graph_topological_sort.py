#TOPOLOGICAL SORT IMPLEMENTATION

from collections import defaultdict


class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)


    def topologicalSortUtil(self, vertex, visited, stack):
        #calling for all adjacent nodes for the vertex
        visited.append(vertex)

        for i in self.graph[vertex]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        stack.insert(0, vertex)
    
    def tologicalSort(self):

        visited_list = []
        stack = []

        for k in list(self.graph):
            #loop through all keys in dict
            if k not in visited_list:
                self.topologicalSortUtil(k, visited_list, stack)
        
        print(stack)


custom_graph = Graph(8)
custom_graph.addEdge('A', 'C')
custom_graph.addEdge('C','E')
custom_graph.addEdge('E','H')
custom_graph.addEdge('E','F')
custom_graph.addEdge('F','G')
custom_graph.addEdge('B','C')
custom_graph.addEdge('B','D')
custom_graph.addEdge('D','F')


print('\n\n')
print(custom_graph.graph)

print('\n\n')
custom_graph.tologicalSort()