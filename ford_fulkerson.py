from collections import defaultdict, deque

def bfs(residual_graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    parent.clear()
    while queue:
        u = queue.popleft()
        for v, capacity in residual_graph[u].items():
            if v not in visited and capacity > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(graph, source, sink):
    residual_graph = defaultdict(lambda: defaultdict(int))
    for u in graph:
        for v, capacity in graph[u].items():
            residual_graph[u][v] += capacity
            if v not in residual_graph[u]:
                residual_graph[v][u] = 0
    max_flow = 0
    parent = {}
    while bfs(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow
