BEGIN
Define the graph using adjacency lists.
Create an empty VISITED set.
Define function DFS(GRAPH, NODE):
If NODE is not present in VISITED:
 Display NODE.
Add NODE to VISITED.
 Get all adjacent nodes of NODE.
For each NEIGHBOR in GRAPH[NODE]:
 If NEIGHBOR is not present in VISITED:
Call DFS(GRAPH, NEIGHBOR).
 End For
End If
END FUNCTION
Call DFS(GRAPH, 1).
Continue until all reachable nodes are visited.
END
