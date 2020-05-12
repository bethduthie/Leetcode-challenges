def reverse(x: int):
    p = 2**31-1
    n = -2**31
    x = str(x)
    y = x[1:]
    if x[0] == '-':
        x = x[0] + y[::-1]
    else:
        x = x[::-1]

    x = int(x)

    if x > p or x < n:
        return 0
    else:
        return x


answer = reverse(12345)
print(answer)
