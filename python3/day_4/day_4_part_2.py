# 1 1 1 1
# 1 1 1 2
# 1 1 1 3
# 1 1 1 4
# 1 1 2 2
# 1 1 2 3
# 1 1 2 4
# 1 1 3 3
# 1 1 3 4
# 1 1 4 4


# 1 1
# 1 2
# 2 2

# 1 1 1
# 1 1 2
# 1 2 2
# 2 2 2


# 1 1 1
# 1 1 2
# 1 1 3
# 1 2 2
# 1 3 3

# 444444-800000


def is_valid_passcode(passcode: int) -> bool:
    # print(f'passcode = {passcode}')
    digit = -1
    adjacent = False
    adjacent_number = -1
    for power in range(5, -1, -1):
        val = passcode // (10 ** power)
        val = val % 10
        # print(val)
        if val < digit:
            return False
        if val == digit:
            if adjacent:
                if val == adjacent_number:
                    adjacent = False
            else:
                if val != adjacent_number:
                    adjacent = True
                    adjacent_number = val
        else:
            adjacent_number = -1
        digit = val

    return adjacent


def naive_counter(from_num, to_num):
    counter = 0
    for x in range(from_num, to_num):
        print(f'{x}: {is_valid_passcode(x)}')
        if is_valid_passcode(x):
            counter += 1
    return counter


if __name__ == '__main__':
    print(is_valid_passcode(112233))
    print(is_valid_passcode(123444))
    print(is_valid_passcode(112222))
    print(is_valid_passcode(778888))
    print(is_valid_passcode(778889))
    print(naive_counter(444444, 800000))
    # print(is_valid_passcode(111122))
    # print(is_valid_passcode(444445))
    # print(is_valid_passcode(456788))
    # print(is_valid_passcode(444488))
    # print(is_valid_passcode(444888))

