# PRIM'S ALGORITHM
'''
    Start with a source vertex: (src = 0, other vertices= INF)
        for all src's adjacent vertices:
            If Cost from src to adjacent vertex is LESS then their weight 
                Update vertex's weight to cost of path
            
            Mark src as visited
            Trace path from src to LEAST WEIGHT VERTEX
        
            this LEAST WEIGHT VERTEC becomes the src
        for all src's adjacent vertes:
            repeat above till all vertices are visited 
            
'''

import sys


# to use sys.maxsize which is infinity

class Graph:
    def __init__(self, num_vertices, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.num_vertex = num_vertices
        self.MST = []

    def print_solution(self):
        print("Edges  :  Weight")
        for src, dest, weight in self.MST:
            print("%s -> %s : %s" % (src, dest, weight))

    def prims_algorithm(self):
        visited_nodes = [0] * self.num_vertex
        edge_number = 0

        visited_nodes[0] = True
        # marking 1st node as visited

        while edge_number < self.num_vertex - 1:
            min_weight = sys.maxsize

            for i in range(self.num_vertex):
                if visited_nodes[i]:
                    # if the vertex is visited
                    # search for adjacent vertices, if they are not
                    # visited and there exist an edge, we find the minimum
                    # edge

                    for j in range(self.num_vertex):
                        if (not visited_nodes[j]) and self.edges[i][j]:
                            if min_weight > self.edges[i][j]:
                                min_weight = self.edges[i][j]

                                src, dest = i, j

            self.MST.append([self.nodes[src], self.nodes[dest], self.edges[src][dest]])
            visited_nodes[dest] = True
            edge_number += 1

        self.print_solution()


# passing a adjacency matrx for edges parameter

edges = [
    [0, 10, 20, 0, 0],
    [10, 0, 30, 5, 0],
    [20, 30, 0, 15, 6],
    [0, 5, 15, 0, 8],
    [0, 0, 6, 8, 0]
]

nodes = ['A', 'B', 'C', 'D', 'E']

custom_graph = Graph(5, edges, nodes)

custom_graph.prims_algorithm()
