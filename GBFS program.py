BEGIN
Define graph and heuristic values
 FUNCTION GBFS(start, goal)
Initialize OPEN list with start node
 Initialize VISITED list as empty
WHILE OPEN list is not empty
Sort OPEN list by heuristic value
Remove node with lowest heuristic value
IF node = goal
  PRINT path
  RETURN
 IF node is not visited
   Add node to VISITED list
 FOR each neighbor of node
IF neighbor is not visited
Add neighbor and updated path to OPEN list
PRINT "Path not found"
Call GBFS(start, goal)
END
