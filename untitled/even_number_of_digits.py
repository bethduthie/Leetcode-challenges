def findNumbers(numbers = []):
    even_nums = []
    for num in numbers:
        num = str(num)
        if len(num) % 2 == 0:
            even_nums.append(num)
    return len(even_nums)


print(findNumbers([1, 11, 123, 12]))
