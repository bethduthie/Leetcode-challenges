def numJewelsInStones(J, S):
    total = 0
    for stone in S:
        if stone in J:
            total += 1
    return total

