from typing import List, Tuple


DIRECTION = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [1, 0],
    'D': [-1, 0],
}

WireCoordinates = List[Tuple[int, Tuple[int, int], int]]


def get_closest_travel_distance_of_intersection(wire1: List[str], wire2: List[str]) -> int:
    wire1_vertical, wire1_horizontal = get_wire_coordinates(wire1)
    wire2_vertical, wire2_horizontal = get_wire_coordinates(wire2)

    intersections = get_intersection_lengths(wire1_horizontal, wire2_vertical) + get_intersection_lengths(wire2_horizontal, wire1_vertical)

    return min(intersections)


def get_wire_coordinates(wire: List[str]) -> (WireCoordinates, WireCoordinates):
    global DIRECTION
    x: int = 0
    y: int = 0
    total_length: int = 0
    vertical_coords: WireCoordinates = []
    horizontal_coords: WireCoordinates = []

    for action in wire:
        direction = action[0]
        distance = int(action[1:])
        new_x = x + (distance * DIRECTION[direction][0])
        new_y = y + (distance * DIRECTION[direction][1])
        if direction in 'RL':
            horizontal_coords.append((new_x, (y, new_y), total_length))
        else:
            vertical_coords.append((new_y, (x, new_x), total_length))
        x = new_x
        y = new_y
        total_length += distance

    return horizontal_coords, vertical_coords


def get_intersection_lengths(horizontal_coords: WireCoordinates, vertical_coords: WireCoordinates) -> List[int]:
    intersections: List[int] = []

    for h_coord in horizontal_coords:
        for v_coord in vertical_coords:
            if min(h_coord[1]) < v_coord[0] < max(h_coord[1]) and min(v_coord[1]) < h_coord[0] < max(v_coord[1]):
                travel_distance1 = v_coord[2] + abs(abs(h_coord[0]) - abs(v_coord[1][0]))
                travel_distance2 = h_coord[2] + abs(abs(v_coord[0]) - abs(h_coord[1][0]))
                intersections.append(travel_distance1 + travel_distance2)

    return intersections


if __name__ == '__main__':
    wire1 = 'R8,U5,L5,D3'
    wire2 = 'U7,R6,D4,L4'
    print(get_closest_travel_distance_of_intersection(wire1.split(','),wire2.split(',')))

    wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    print(get_closest_travel_distance_of_intersection(wire1.split(','),wire2.split(',')))

    wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    print(get_closest_travel_distance_of_intersection(wire1.split(','),wire2.split(',')))

    with open('input.txt') as f:
        lines = f.readlines()
        wire1 = lines[0]
        wire2 = lines[1]
        print(get_closest_travel_distance_of_intersection(wire1.split(','),wire2.split(',')))
