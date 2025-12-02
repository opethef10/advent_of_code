def part1(lines, text):
    first, second = [], []
    for line in lines:
        a, b = line.split()
        first.append(int(a))
        second.append(int(b))
    first.sort()
    second.sort()

    total_1 = sum(abs(s - f) for f, s in zip(first, second))
    total_2 = sum(f * second.count(f) for f in first)
    return total_1, total_2


def part2(lines, text):
    return
