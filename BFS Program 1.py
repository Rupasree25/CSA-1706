graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E', 'F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
visited = []
queue = ['A']
while queue:
   node = queue.pop(0)
   if node not in visited:
   visited.append(node)
queue.extend(x for x in graph[node] if x not in visited)
print("BFS Traversal:", visited)
