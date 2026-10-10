BEGIN
Define the graph with nodes and edge costs.
Define function UCS(GRAPH, START, GOAL):
  Create an empty priority queue.
Insert (0, START, [START]) into the queue.
Create an empty VISITED set.
WHILE the priority queue is not empty:
Remove the element with the lowest cost.
If NODE is equal to GOAL:
  Display PATH.
  Display TOTAL COST.
 Return.
If NODE is not in VISITED:
Add NODE to VISITED.
FOR each NEIGHBOR and WEIGHT in GRAPH[NODE]:
If NEIGHBOR is not in VISITED:
  NEW_COST = COST + WEIGHT.
  NEW_PATH = PATH + NEIGHBOR.
Insert (NEW_COST, NEIGHBOR, NEW_PATH)
into the priority queue.
  END FOR
  END WHILE
  END FUNCTION
Call UCS(GRAPH, 'S', 'G').
END
