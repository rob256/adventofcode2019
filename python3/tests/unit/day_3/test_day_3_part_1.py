import pytest

from day_3 import day_3_part_1


def test_get_closest_manhattan_distance_of_intersection():
    pass


@pytest.mark.parametrize(('wire_actions', 'expected'), [
    (['R1'], ([(0, (0, 1))], [])),
    (['L1'], ([(0, (-1, 0))], [])),
    (['L1', 'U3', 'L3'], ([(0, (-1, 0)), (3, (-4, -1))], [(-1, (0, 3))])),
])
def test_get_wire_coordinates(wire_actions, expected):
    assert day_3_part_1.get_wire_coordinates(wire_actions) == expected


def test_intersections():
    v_coords = [(5, (0, 100))]
    h_coords = [(10, (0, 100))]
    assert day_3_part_1.get_intersections(h_coords, v_coords) == [(5, 10)]
