from typing import List


def process_intcode_string(intcode_str: str, input_diagnostic: int) -> str:
    intcode = list(map(int, intcode_str.split(',')))
    return ','.join(str(x) for x in process_intcode(intcode, input_diagnostic))


def process_intcode(intcode: List[int], input_diagnostic: int) -> List[int]:
    stored_input: int = input_diagnostic
    pos: int = 0
    while True:
        proc_code = intcode[pos]
        modes = {}
        if proc_code == 99:
            break

        if proc_code > 99:
            _proc_code = proc_code % 100
            modes[1] = proc_code // 100 % 10
            modes[2] = proc_code // 1000 % 10
            modes[3] = proc_code // 10000 % 10
            proc_code = _proc_code

        if proc_code == 1:
            pos1 = intcode[(pos + 1) % len(intcode)]
            pos2 = intcode[(pos + 2) % len(intcode)]
            target_pos = intcode[(pos + 3) % len(intcode)]
            num1 = intcode[pos1] if modes.get(1, 0) == 0 else pos1
            num2 = intcode[pos2] if modes.get(2, 0) == 0 else pos2
            intcode[target_pos] = num1 + num2
            move_pos = 4
            print(f'ADD {pos1} ({num1}) + {pos2} ({num2}) = {target_pos} ({num1 + num2})')
        elif proc_code == 2:
            pos1 = intcode[(pos + 1) % len(intcode)]
            pos2 = intcode[(pos + 2) % len(intcode)]
            target_pos = intcode[(pos + 3) % len(intcode)]
            num1 = intcode[pos1] if modes.get(1, 0) == 0 else pos1
            num2 = intcode[pos2] if modes.get(2, 0) == 0 else pos2
            intcode[target_pos] = num1 * num2
            move_pos = 4
            print(f'MULTIPLY {pos1} ({num1}) * {pos2} ({num2}) = {target_pos} ({num1 + num2})')
        elif proc_code == 3:
            pos1 = intcode[(pos + 1) % len(intcode)]
            num1 = stored_input
            intcode[pos1] = num1
            move_pos = 2
            print(f'STORE {pos1} ({num1})')
        elif proc_code == 4:
            pos1 = intcode[(pos + 1) % len(intcode)]
            num1 = intcode[pos1] if modes.get(1, 0) == 0 else pos1
            print(intcode[pos1])
            move_pos = 2
            print(f'SAVE {pos1} ({num1})')
        elif proc_code == 5:
            pos1 = intcode[(pos + 1) % len(intcode)]
            num1 = intcode[pos1] if modes.get(1, 0) == 0 else pos1
            pos2 = intcode[(pos + 2) % len(intcode)]
            num2 = intcode[pos2] if modes.get(2, 0) == 0 else pos2
            if num1 != 0:
                pos = num2
                move_pos = 0
            else:
                move_pos = 3
            print(f'JUMP-IF-TRUE {pos1} ({num1}) {pos2} ({num2})')
        elif proc_code == 6:
            pos1 = intcode[(pos + 1) % len(intcode)]
            num1 = intcode[pos1] if modes.get(1, 0) == 0 else pos1
            pos2 = intcode[(pos + 2) % len(intcode)]
            num2 = intcode[pos2] if modes.get(2, 0) == 0 else pos2
            if num1 == 0:
                pos = num2
                move_pos = 0
            else:
                move_pos = 3
            print(f'JUMP-IF-FALSE {pos1} ({num1}) {pos2} ({num2})')
        elif proc_code == 7:
            pos1 = intcode[(pos + 1) % len(intcode)]
            num1 = intcode[pos1] if modes.get(1, 0) == 0 else pos1
            pos2 = intcode[(pos + 2) % len(intcode)]
            num2 = intcode[pos2] if modes.get(2, 0) == 0 else pos2
            target_pos = intcode[(pos + 3) % len(intcode)]
            if num1 < num2:
                intcode[target_pos] = 1
            else:
                intcode[target_pos] = 0
            move_pos = 4
            print(f'LESS-THAN {pos1} ({num1}) < {pos2} ({num2}) = {target_pos}')
        elif proc_code == 8:
            pos1 = intcode[(pos + 1) % len(intcode)]
            num1 = intcode[pos1] if modes.get(1, 0) == 0 else pos1
            pos2 = intcode[(pos + 2) % len(intcode)]
            num2 = intcode[pos2] if modes.get(2, 0) == 0 else pos2
            target_pos = intcode[(pos + 3) % len(intcode)]
            if num1 == num2:
                intcode[target_pos] = 1
            else:
                intcode[target_pos] = 0
            move_pos = 4
            print(f'EQUAL TO {pos1} ({num1}) == {pos2} ({num2}) = {target_pos}')
        else:
            raise ValueError(f'proc_code {proc_code} not recognised in position {pos} for intcode {intcode}')

        pos = (pos + move_pos) % len(intcode)

    return intcode


if __name__ == '__main__':
    # process_intcode_string('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 0)
    # process_intcode_string('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 1)
    # process_intcode_string('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 0)
    # process_intcode_string('1101,100,-1,4,0')
    with open('input.txt') as f:
        intcode_str = f.read()
        intcode = list(map(int, intcode_str.split(',')))
        #19690720
        # intcode[1] = 82
        # intcode[2] = 26
        intcode = process_intcode(intcode, 5)
        # print(intcode[0])
        print(intcode)