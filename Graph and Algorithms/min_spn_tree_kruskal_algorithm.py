#KRUSKAL'S ALGORITHM
'''
    Find the path having Minimum Cost
    Trace the path if they do not form a cycle:
        Check if src and dest vertices have the same parent in disjoin set
        If they do, Union of src and dest will result in repetition of vertices
        resulting in a cycle
        IF NOT
            trace path from src to dest
    Repeat above step with the next minimum path
    CONTINUE till all vertices are visited
    in the end all vertices will have the same rootNode (parent)

'''

import min_spn_tree_disjoint_set as dst


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []
        self.MST = []
            #MST: min spnng tree
        
    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])
    
    def add_node(self, node_value):
        self.nodes.append(node_value)
    
    def print_solution(self):
        for src, dest, weight in self.MST:
            print("%s  ->  %s:  %s" %(src, dest, weight))

    def kruskal_algorithm(self):
        i, e = 0,0

        ds = dst.Disjoint_Set(self.nodes)

        self.graph = sorted(self.graph, key = lambda item: item[2])
            #sort the graph according to the weight
        
        while e < self.vertices - 1:
            src, dest, weight = self.graph[i]
            #loop through min to max paths
            i += 1

            x_root = ds.find_parent(src)
                #find parent of src
            y_root = ds.find_parent(dest)

            if x_root != y_root:
                #different parents => no cycle
                e += 1
                #adding edge
                self.MST.append([src, dest, weight])
                ds.union(x_root, y_root)
            
        #printing output
        self.print_solution()


custom_graph = Graph(5)

custom_graph.add_node('A')
custom_graph.add_node('B')
custom_graph.add_node('C')
custom_graph.add_node('D')
custom_graph.add_node('E')

custom_graph.add_edge('A', 'B', 5)
custom_graph.add_edge('B', 'A', 5)
    #since we have undirected graph => A->B and B->A
custom_graph.add_edge('B', 'D', 8)
custom_graph.add_edge('D', 'B', 8)
custom_graph.add_edge('B', 'C', 10)
custom_graph.add_edge('C', 'B', 10)
custom_graph.add_edge('A', 'C', 13)
custom_graph.add_edge('C', 'A', 13)
custom_graph.add_edge('A', 'E', 15)
custom_graph.add_edge('E', 'A', 15)
custom_graph.add_edge('C', 'E', 20)
custom_graph.add_edge('E', 'C', 20)
custom_graph.add_edge('C', 'D', 6)
custom_graph.add_edge('D', 'C', 6)

custom_graph.kruskal_algorithm()

