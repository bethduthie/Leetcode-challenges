def numOfSteps(num):
    amount_of_steps = 0
    if num == 0:
        return amount_of_steps
    if num >= 1000000:
        return 'That number is too big.'
    if num < 0:
        return 'Number cannot be a negative.'
    while num > 0:
        if num % 2 == 0:
            num = num / 2
            amount_of_steps += 1
        else:
            num = num - 1
            amount_of_steps += 1
    return amount_of_steps


print(numOfSteps(12333333))
