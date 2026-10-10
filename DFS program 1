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
def dfs(node):
   if node not in visited:
      visited.append(node)
      for x in graph[node]:
        dfs(x)
dfs('A')
print("DFS Traversal:", visited)
