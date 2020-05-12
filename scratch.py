def my_func(string):
    for i in range(len(string)):
        if i % 2 == 0:
            string[i].upper()
            result += string.upper()[i]
        else:
            string[i].upper()
            result += string.lower()[i]
    return result


print(my_func('hello'))
