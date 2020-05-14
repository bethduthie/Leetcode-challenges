def sortedSquares(a):
    squared_nums = []
    for num in a:
        squared = num * num
        squared_nums.append(squared)
    squared_nums.sort()
    return squared_nums
