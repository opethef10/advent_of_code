THRESHOLD = 3


def safety_check(report):
    deltas = []
    for a, b in zip(report[:-1], report[1:]):
        deltas.append(b - a)
    jump = all(0 < abs(d) <= THRESHOLD for d in deltas)
    asc = any(d > 0 for d in deltas)
    desc = any(d < 0 for d in deltas)

    if not jump:
        return False

    if asc and desc:
        return False
    return True


def part1(lines, text):
    safe = 0
    for line in lines:
        report = list(map(int, line.split()))
        safe += int(safety_check(report))

    return safe


def part2(lines, text):
    return
