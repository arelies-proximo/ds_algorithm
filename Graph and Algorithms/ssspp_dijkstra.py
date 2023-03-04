from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[ (fromNode, toNode) ] = distance


def dijkstra(graph, initialNode):
    visited = {initialNode: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[minNode, edge]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    print('Shortest Path from ',initialNode,' to:\n')
    print(visited)

    print('\nPath: \n')
    print(path)
    return


custom_graph = Graph()
custom_graph.addNode('A')
custom_graph.addNode('B')
custom_graph.addNode('C')
custom_graph.addNode('D')
custom_graph.addNode('E')
custom_graph.addNode('F')
custom_graph.addNode('G')

#adding edges
custom_graph.addEdge('A', 'B', 2)
custom_graph.addEdge('A', 'C', 5)
custom_graph.addEdge('B', 'C', 6)
custom_graph.addEdge('B', 'D', 1)
custom_graph.addEdge('B', 'E', 3)
custom_graph.addEdge('C', 'F', 8)
custom_graph.addEdge('D', 'E', 4)
custom_graph.addEdge('E', 'G', 9)
custom_graph.addEdge('F', 'G', 7)

print('Nodes: ',custom_graph.nodes)
print('\n\nEdges: ',custom_graph.edges)
print('\n\nDistances: ',custom_graph.distances)

print('\n\n')
dijkstra(custom_graph, 'B')

