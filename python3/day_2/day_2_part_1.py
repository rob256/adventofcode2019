from typing import List


def process_intcode_string(intcode_str: str) -> str:
    intcode = list(map(int, intcode_str.split(',')))
    return ','.join(str(x) for x in process_intcode(intcode))


def process_intcode(intcode: List[int]) -> List[int]:
    pos: int = 0
    while True:
        proc_code = intcode[pos]
        if proc_code == 99:
            break
        pos1 = intcode[(pos + 1) % len(intcode)]
        pos2 = intcode[(pos + 2) % len(intcode)]
        target_pos = intcode[(pos + 3) % len(intcode)]
        num1 = intcode[pos1]
        num2 = intcode[pos2]

        if proc_code == 1:
            intcode[target_pos] = num1 + num2
        elif proc_code == 2:
            intcode[target_pos] = num1 * num2
        else:
            raise ValueError(f'proc_code {proc_code} not recognised in position {pos} for intcode {intcode}')

        pos = (pos + 4) % len(intcode)

    return intcode


if __name__ == '__main__':
    with open('input.txt') as f:
        intcode_str = f.read()
        intcode = list(map(int, intcode_str.split(',')))
        intcode[1] = 12
        intcode[2] = 2
        intcode = process_intcode(intcode)
        print(intcode[0])
