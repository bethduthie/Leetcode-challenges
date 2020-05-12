def subtractProductAndSum(self, num):
    if num <= 1:
        0
    if num >= 10 ** 5:
        0
    else:
        num = str(num)
        first_digit = int(num[0])

        if len(num) == 1:
            return 0

        if len(num) == 2:
            second_digit = int(num[1])
            product = first_digit * second_digit
            addition = first_digit + second_digit
        if len(num) == 3:
            second_digit = int(num[1])
            third_digit = int(num[2])
            product = first_digit * second_digit * third_digit
            addition = first_digit + second_digit + third_digit
        if len(num) == 4:
            second_digit = int(num[1])
            third_digit = int(num[2])
            fourth_digit = int(num[3])
            product = first_digit * second_digit * third_digit * fourth_digit
            addition = first_digit + second_digit + third_digit + fourth_digit
        if len(num) == 5:
            second_digit = int(num[1])
            third_digit = int(num[2])
            fourth_digit = int(num[3])
            fifth_digit = int(num[4])
            product = first_digit * second_digit * third_digit * fourth_digit * fifth_digit
            addition = first_digit + second_digit + third_digit + fourth_digit + fifth_digit

    subtract = product - addition
    return subtract
