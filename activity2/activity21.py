class CustomGraph:
    def __init__(self):
        self.vertices_and_neighbors = {}

    def add_node(self, node):
        if node not in self.vertices_and_neighbors:
            self.vertices_and_neighbors[node] = []

    def add_link(self, node1, node2):
        if node1 in self.vertices_and_neighbors and node2 in self.vertices_and_neighbors:
            self.vertices_and_neighbors[node1].append(node2)
            self.vertices_and_neighbors[node2].append(node1)

    def depth_first_search(self, start_node, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_node)
        print(start_node, end=" ")

        for neighbor in self.vertices_and_neighbors[start_node]:
            if neighbor not in visited:
                self.depth_first_search(neighbor, visited)
