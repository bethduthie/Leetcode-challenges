def kidsWithCandies(candies, extra_candies):
    most_with_extras = []
    for kid in candies:
        if kid + extra_candies >= max(candies):
            most_with_extras.append(True)
        else:
            most_with_extras.append(False)
    return most_with_extras


print(kidsWithCandies([2, 3, 4, 1], 3))
