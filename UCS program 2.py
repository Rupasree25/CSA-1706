BEGIN
Define the graph with nodes and edge costs.
Define function UCS(GRAPH, START, GOAL):
 Create a priority queue.
Insert (0, START, [START]) into the queue.
 Create an empty VISITED set.
WHILE the queue is not empty:
 Remove the path with the lowest total cost.
 If NODE is equal to GOAL:
    Display the PATH.
    Display the TOTAL COST.
     Return.
 If NODE is not present in VISITED:
 Add NODE to VISITED.
FOR each NEIGHBOR and WEIGHT in GRAPH[NODE]:
 If NEIGHBOR is not present in VISITED:
     Calculate NEW_COST = COST + WEIGHT.
 Create a new path by adding NEIGHBOR.
   Insert (NEW_COST, NEIGHBOR, NEW_PATH)
into the priority queue.
 END FOR
  END WHILE
END FUNCTION
Call UCS(GRAPH, 'V1', 'V6').
END
