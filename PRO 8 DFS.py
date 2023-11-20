from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start, visited):
        if start not in visited:
            print(start, end=" ")
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs(neighbor, visited)

    def dfs_start(self, start):
        visited = set()
        print(f"DFS starting from node {start}:")
        self.dfs(start, visited)

if __name__ == "__main__":
    # Example graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    start_node = 0
    g.dfs_start(start_node)
