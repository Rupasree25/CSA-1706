BEGIN
    Define the game tree with leaf values
    Initialize ALPHA = -∞
    Initialize BETA = +∞
FUNCTION ALPHABETA(depth, node, alpha, beta, is_max)
IF depth = 2
 RETURN leaf value of node
  IF is_max = TRUE
   value = -∞
 FOR each child of node
 value = MAX(value, ALPHABETA(
 depth + 1, child, alpha, beta, FALSE))
   alpha = MAX(alpha, value)
 IF alpha >= beta
     BREAK
 RETURN value
ELSE
  value = +∞
 FOR each child of node
 value = MIN(value, ALPHABETA(
 depth + 1, child, alpha, beta, TRUE))
  beta = MIN(beta, value)
 IF beta <= alpha
   BREAK
 RETURN value
result = ALPHABETA(0, root, ALPHA, BETA, TRUE)
    PRINT result
END
