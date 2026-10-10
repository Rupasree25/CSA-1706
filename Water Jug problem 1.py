jug1 = 0
jug2 = 0
while jug1 != 4:
    if jug1 == 0:
        jug1 = 5
    elif jug2 < 3 and jug1 > 0:
        transfer = min(jug1, 3 - jug2)
        jug1 -= transfer
        jug2 += transfer
    elif jug2 == 3:
        jug2 = 0
    print("5L jug:", jug1, "3L jug:", jug2)
print("Target of 4 litres reached!")
