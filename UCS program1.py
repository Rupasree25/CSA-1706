import heapq
graph = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 2)],
    'C': [('B', 1), ('G', 2)],
    'D': [('G', 3)],
    'G': []
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
ucs('S', 'G')
