START_POINT = 50
NUM_POSITIONS = 100


def part1(lines, text):
    total_zeroes = 0
    current_position = START_POINT
    for line in lines:
        direction, value = line[0], int(line[1:])
        if direction == "L":
            current_position -= value
        elif direction == "R":
            current_position += value
        current_position %= NUM_POSITIONS
        if current_position == 0:
            total_zeroes += 1
    return total_zeroes


def part2(lines, text):
    return
