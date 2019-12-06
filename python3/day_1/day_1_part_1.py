def calculate_fuel(mass: int) -> int:
    mass //= 3
    mass -= 2
    return mass


def calculate_total_fuel_for_file(input_file: str) -> int:
    total_fuel: int = 0

    with open(input_file) as f:
        for line in f:
            total_fuel += calculate_fuel(int(line))

    return total_fuel


if __name__ == '__main__':
    print(calculate_total_fuel_for_file('day1.txt'))