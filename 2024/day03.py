#! /usr/bin/env/python
import re

from utils import input_text, input_lines

PATTERN = re.compile(r"mul\((\d+),(\d+)\)")

if __name__ == "__main__":
    text = input_text(__file__)

    matches = PATTERN.findall(text)
    result = sum(int(l) * int(r) for l, r in matches)
    print(result)
