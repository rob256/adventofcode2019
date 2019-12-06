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
    print(f'passcode = {passcode}')
    digit = -1
    adjacent = False
    for power in range(5, -1, -1):
        val = passcode // (10 ** power)
        val = val % 10
        # print(val)
        if val < digit:
            return False
        if val == digit:
            adjacent = True
        digit = val
    return adjacent


def naive_counter(from_num, to_num):
    counter = 0
    for x in range(from_num, to_num):
        if is_valid_passcode(x):
            counter += 1
    return counter


if __name__ == '__main__':
    print(is_valid_passcode(123456))
    print(is_valid_passcode(1134))
    print(naive_counter(444444, 800000))
    # print(is_valid_passcode(444444))
    # print(is_valid_passcode(444445))
    # print(is_valid_passcode(456788))

