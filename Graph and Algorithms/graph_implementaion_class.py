#GRAPH IMPLEMENTATION

class Graph:
    def __init__(self, gr_dict= None):
        if gr_dict is None:
            gr_dict = {}
        self.gr_dict = gr_dict

    def add_edge(self, vertex, edge):
        self.gr_dict[vertex].append(edge)
        #add edge node to list of edges of key

    def bfs(self, vertex):
        #vertex: node to start with
        visited_list = [vertex]
        queue = [vertex]

        while queue:
            deq_vertex = queue.pop(0)  #del from front

            print(deq_vertex, end=" ")
            for adjacentVertex in self.gr_dict[deq_vertex]:
                if adjacentVertex not in visited_list:
                    visited_list.append(adjacentVertex)
                    queue.append(adjacentVertex)    #add at rear
        print()


    def dfs(self, vertex):
        visited_list = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop() #return last item
            print(popVertex, end=" ")
            for adjacentVertex in self.gr_dict[popVertex]:
                if adjacentVertex not in visited_list:
                    visited_list.append(adjacentVertex)
                    stack.append(adjacentVertex)
        print()





customDict = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['b', 'e', 'f'],
    'e': ['d', 'f', 'c'],
    'f': ['d', 'e']
}

graph = Graph(customDict)
print(graph.gr_dict, end='\n\n')

#printing edge of 'a'
print(graph.gr_dict['a'])


graph.dfs('a')