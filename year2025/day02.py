def is_number_invalid(num: int) -> bool:
    str_int = str(num)
    length = len(str_int)
    if length % 2 != 0:
        return False
    half = length // 2
    first_half = str_int[:half]
    second_half = str_int[half:]
    return first_half == second_half


def part1(lines: list[str], text: str) -> int:
    total = 0
    ranges = text.split(',')
    for rng_str in ranges:
        rng = range(int(rng_str.split('-')[0]), int(rng_str.split('-')[1]) + 1)
        for num in rng:
            if is_number_invalid(num):
                total += num
    return total


def part2(lines: list[str], text: str) -> int:
    pass
