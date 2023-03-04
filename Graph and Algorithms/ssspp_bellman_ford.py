#BELLMAN FORD SSSPP

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, dict, source):
        print("\n\nVertex Distance from Source", source, " to: ")
        for key, value in dict.items():
            print(' ',key,' : ', value)
    

    def bellman_ford(self, source):
        dict = {i : float('Inf') for i in self.nodes}

        dict[source] = 0

        for _ in range(self.num_vertices):
            for src, dest, wht, in self.graph:
                if dict[src] != float('Inf') and dict[src] + wht < dict[dest]:
                    dict[dest] = dict[src] + wht

        #for checking negative cycle
        #run the loop agn, if change occurs: neg cycle is present

        for src, dest, wht in self.graph:
            if dict[src] != float('Inf') and dict[src] + wht < dict[dest]:
                print('Graph contains negative Cycle.')
        

        self.print_solution(dict, source)



custom_graph = Graph(5)
custom_graph.add_node('A')
custom_graph.add_node('B')
custom_graph.add_node('C')
custom_graph.add_node('D')
custom_graph.add_node('E')

custom_graph.add_edge('A', 'C', 6)
custom_graph.add_edge('A', 'D', 6)
custom_graph.add_edge('B', 'A', 3)
custom_graph.add_edge('C', 'D', 1)
custom_graph.add_edge('D', 'C', 2)
custom_graph.add_edge('D', 'B', 1)
custom_graph.add_edge('E', 'B', 4)
custom_graph.add_edge('E', 'D', 2)

custom_graph.bellman_ford('E')