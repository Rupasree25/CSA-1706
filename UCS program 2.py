import heapq
graph = {
    'V1': [('V2', 9), ('V3', 4)],
    'V2': [('V3', 5), ('V4', 7), ('V5', 3)],
    'V3': [('V4', 2), ('V5', 6)],
    'V4': [('V5', 4), ('V6', 8)],
    'V5': [('V6', 2)],
    'V6': []
}
def ucs(start, goal):
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == goal:
            print("Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        queue,
                        (cost + weight, neighbor, path + [neighbor])
                    )
ucs('V1', 'V6')
