from collections import deque
graph = {
    1: [2, 3],
    2: [3, 4, 5],
    3: [5],
    4: [5],
    5: []
}
visited = set()
queue = deque([1])
while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
