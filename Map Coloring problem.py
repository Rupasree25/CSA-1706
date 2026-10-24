BEGIN
Define graph with regions and neighbors
Define available colors
 Initialize color_map as empty
  FUNCTION IS_SAFE(region, color)
    FOR each neighbor of region
    IF neighbor has the same color
   RETURN FALSE
    RETURN TRUE
 FUNCTION SOLVE(regions)
   IF all regions are colored
    RETURN TRUE
Select the next region
FOR each color in available colors
   IF IS_SAFE(region, color)
  Assign color to region
  IF SOLVE(remaining regions)
    RETURN TRUE
  Remove assigned color (Backtrack)
RETURN FALSE
 IF SOLVE(all regions)
 PRINT color_map
   ELSE
 PRINT "No solution exists"
END
