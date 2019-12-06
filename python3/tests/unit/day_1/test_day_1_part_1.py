from os.path import dirname

import pytest

from day_1 import day_1_part_1


@pytest.mark.parametrize(('mass', 'fuel'), [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
])
def test_calculate_fuel(mass, fuel):
    assert day_1_part_1.calculate_fuel(mass) == fuel


TEST_DIR = dirname(__file__)


def test_sum_fuel():
    assert day_1_part_1.calculate_total_fuel_for_file(TEST_DIR + "/day_1_part_1_input.txt") == 2 + 2 + 654 + 33583