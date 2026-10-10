BEGIN
Initialize JUG1 = 0.
Initialize JUG2 = 0.
WHILE JUG1 is not equal to 4:
 IF JUG1 is equal to 0:
 Fill JUG1 completely with 5 litres.
 ELSE IF JUG2 is less than 3 AND JUG1 is greater than 0:
 Calculate TRANSFER = minimum of JUG1
 and (3 - JUG2).
 Subtract TRANSFER from JUG1.
 Add TRANSFER to JUG2.
 ELSE IF JUG2 is equal to 3:
  Empty JUG2 completely.
  END IF
Display the amount of water in both jugs.
END WHILE
Display "Target of 4 litres reached!"
END
