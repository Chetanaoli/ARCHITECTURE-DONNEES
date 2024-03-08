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

    def show_graph(self):
        for node, neighbors in self.vertices_and_neighbors.items():
            print(f"{node}: {neighbors}")
