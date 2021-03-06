class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for ver, val in self.adj_list.items():
            print(ver, ':', val)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertix(self, vertix):
        if vertix in self.adj_list.keys():
            for other_vertix in self.adj_list[vertix]:
                self.adj_list[other_vertix].remove(vertix)
            del self.adj_list[vertix]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)
my_graph.remove_edge(2,3)
my_graph.remove_edge(1,2)

my_graph.print_graph()
