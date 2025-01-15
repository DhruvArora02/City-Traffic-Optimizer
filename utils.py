from collections import defaultdict

def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    n, m = map(int, data[0].split())
    graph = defaultdict(lambda: defaultdict(int))
    for i in range(1, m + 1):
        u, v, capacity = map(int, data[i].split())
        graph[u][v] += capacity
    return graph, n
