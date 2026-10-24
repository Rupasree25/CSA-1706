BEGIN
    Initialize an N × N chessboard
    Set all positions as empty
  FUNCTION IS_SAFE(row, col)
  FOR each previous row
 IF queen is in the same column
    OR same diagonal
   RETURN FALSE
        RETURN TRUE
FUNCTION SOLVE(row)
        IF row = N
            PRINT chessboard
            RETURN TRUE
FOR col = 0 to N - 1
 IF IS_SAFE(row, col)
Place queen at (row, col)
IF SOLVE(row + 1)
  RETURN TRUE
  Remove queen (Backtrack)
  RETURN FALSE
IF SOLVE(0) = FALSE
        PRINT "No solution exists"

END
