BEGIN

1. Initialize the graph with nodes and edge costs.
2. Assign heuristic values to each node.
3. Set the start node A and goal node G.
4. Add the start node to the OPEN list.
5. WHILE OPEN list is not empty:
      a. Select the node with the lowest f value.
      b. Remove the node from the OPEN list.
      c. IF the node is the goal:
            Print the path and total cost.
            STOP.
      d. IF the node is not visited:
            Mark the node as visited.
         FOR each neighbor of the node:
                IF the neighbor is not visited:
                    Calculate g = current cost + edge cost.
                    Calculate f = g + heuristic value.
                    Add the neighbor to the OPEN list.
6. Print "Path not found" if the goal is unreachable.
END
