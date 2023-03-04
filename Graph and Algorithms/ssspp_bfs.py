

class Graph:
    def __init__(self, gr_dict= None):
        if gr_dict is None:
            gr_dict = {}
        self.gr_dict = gr_dict
    
    def bfs(self, start, end):
        queue = []
        queue.append([start])

        while queue:
            path = queue.pop(0)
            node = path[-1]     #brings the last item from list

            if node == end:
                print(path)
                return
            for adjacent in self.gr_dict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


custom_dict = {
    'A': ['B', 'C'],
    'B': ['D', 'G'],
    'C': ['D', 'E'],
    'D': ['C','F'],
    'E': ['F'],
    'F': ['G'],
    'G': ['F']
}

g = Graph(custom_dict)
g.bfs('A', "G")