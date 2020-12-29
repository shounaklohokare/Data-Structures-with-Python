graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):

    queue = [start]
    visited = set()

    while queue:

        vertex = queue.pop(0)

        if vertex not in visited:

            visited.add(vertex)

            queue.extend(graph[vertex] - visited)

    return visited