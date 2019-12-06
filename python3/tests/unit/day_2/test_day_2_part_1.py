import pytest

from day_2 import day_2_part_1


@pytest.mark.parametrize(('intcode_str', 'expected'), [
    ('1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50'),
    ('1,0,0,0,99', '2,0,0,0,99'),
    ('2,3,0,3,99', '2,3,0,6,99'),
    ('2,4,4,5,99,0', '2,4,4,5,99,9801'),
    ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99')
])
def test_process_intcode_str(intcode_str, expected):
    assert day_2_part_1.process_intcode_string(intcode_str) == expected