def roman_nums(s):
    rom_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    try:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            total = rom_nums[s]
            return total

        if s == '':
            return 0

        for i in s:
            cur_val = rom_nums[i]
            total += cur_val
            if prev_value < cur_val:
                total -= (prev_value*2)
            prev_value = cur_val

    except KeyError:
        print('Not a Roman Numeral')

    return total


if __name__ == '__main__':
    print(roman_nums(''))
    print(__name__)
