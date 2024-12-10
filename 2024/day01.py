#! /usr/bin/env python

from utils import input_text, input_lines

if __name__ == "__main__":
    lines = input_lines(__file__)

    first, second = [], []
    for line in lines:
        a, b = line.split()
        first.append(int(a))
        second.append(int(b))
    first.sort()
    second.sort()

    total_1 = sum(abs(s - f) for f, s in zip(first, second))
    total_2 = sum(f * second.count(f) for f in first)
    print(total_1, total_2)
