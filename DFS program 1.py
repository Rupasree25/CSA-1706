DFS(Graph, Node)
1. If Node is not visited:
      a. Add Node to visited list.
      b. For each neighbor in Graph[Node]:
             Call DFS(Graph, neighbor).
2. Stop.
