#! /usr/bin/env/python
from utils import input_text, input_lines

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


if __name__ == "__main__":
    lines = input_lines(__file__)

    safe = 0
    for line in lines:
        report = list(map(int,line.split()))
        safe += int(safety_check(report))

    print(safe)
