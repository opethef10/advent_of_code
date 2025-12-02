import re


PATTERN = re.compile(r"mul\((\d+),(\d+)\)")


def solve(lines, text):
    matches = PATTERN.findall(text)
    result = sum(int(l) * int(r) for l, r in matches)
    return result
