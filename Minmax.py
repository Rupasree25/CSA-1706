BEGIN
Define the game tree with leaf values
FUNCTION MINIMAX(depth, node, is_max)
IF depth = 2
RETURN leaf value of node
 IF is_max = TRUE
  RETURN MAX(
 MINIMAX(depth + 1, left child, FALSE),
MINIMAX(depth + 1, right child, FALSE)
   )
ELSE
 RETURN MIN(
MINIMAX(depth + 1, left child, TRUE),
MINIMAX(depth + 1, right child, TRUE)
   )
SET root node as MAX player
 result = MINIMAX(0, root, TRUE)
PRINT result
END
