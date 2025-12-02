#!/usr/bin/env python
import argparse

from utils import input_path, input_lines, input_text, get_module


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Advent of Code solution")
    parser.add_argument("year", type=int, help="Year of the puzzle")
    parser.add_argument("day", type=int, help="Day of the puzzle")
    parser.add_argument(
        "-e", "--example", action="store_true", help="Use example input"
    )
    args = parser.parse_args()

    input_file_path = input_path(args.year, args.day, args.example)
    lines = input_lines(input_file_path)
    text = input_text(input_file_path)

    module = get_module(args.year, args.day)
    result = module.solve(lines, text)
    print(result)
