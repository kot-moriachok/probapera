from collections import deque


class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.adjacency_list[from_vertex].append(to_vertex)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.adjacency_list.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def adjacency_matrix_from_edges(self, edges):
        vertices = sorted(self.adjacency_list.keys())
        vertex_index = {v: i for i, v in enumerate(vertices)}
        size = len(vertices)
        matrix = [[0] * size for _ in range(size)]

        for from_vertex, to_vertex in edges:
            i = vertex_index[from_vertex]
            j = vertex_index[to_vertex]
            matrix[i][j] = 1
        return matrix

    def adjacency_list_from_edges(self, edges):
        adj_list = {}
        for from_vertex, to_vertex in edges:
            if from_vertex not in adj_list:
                adj_list[from_vertex] = []
            if to_vertex not in adj_list:
                adj_list[to_vertex] = []
            adj_list[from_vertex].append(to_vertex)
        return adj_list


# Тестирование реализации
if __name__ == "__main__":
    # Создаем граф
    graph = DirectedGraph()

    # Добавляем вершины
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')

    # Добавляем ребра
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')

    # Тест BFS
    print("BFS обход начиная с 'A':", graph.bfs('A'))

    # Тест матрицы смежности
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
    print("Матрица смежности:")
    matrix = graph.adjacency_matrix_from_edges(edges)
    for row in matrix:
        print(row)

    # Тест списка смежности
    print("Список смежности:")
    adj_list = graph.adjacency_list_from_edges(edges)
    for vertex, neighbors in adj_list.items():
        print(f"{vertex}: {neighbors}")
