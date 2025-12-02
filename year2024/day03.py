import re


PATTERN = re.compile(r"mul\((\d+),(\d+)\)")


def part1(lines, text):
    matches = PATTERN.findall(text)
    result = sum(int(l) * int(r) for l, r in matches)
    return result


def part2(lines, text):
    return
