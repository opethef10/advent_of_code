# Advent of Code 🎄

Welcome to my solutions for [Advent of Code](https://adventofcode.com), an annual programming event featuring fun and challenging puzzles released daily from December 1st to 25th. This repository contains my Python solutions for various years.

## Repository Structure
- Each year has its own directory (e.g., `year2024/`), which is a Python package.
- Within each year:
  - Solutions are organized as `dayXX.py` files, where `XX` corresponds to the day of the puzzle.
  - Inputs are expected to be stored locally in:
    - `inputs/` for actual puzzle inputs.
    - `example_inputs/` for example inputs provided in the challenge description.
- `utils.py` at the root provides helper functions for common tasks, such as reading inputs, parsing data, or other repetitive operations.
  - `__main__.py` serves as the entry point to run solutions, accepting year and day as an input and an optional `--example` flag to use example inputs instead of actual puzzle inputs.

## Note on Inputs
Puzzle input files are expected to be stored locally in the `inputs/` and `example_inputs/` folders, which are `.gitignore`-protected and not included in the repository to comply with Advent of Code's [Terms of Service](https://adventofcode.com/2024/about). Each solution file (e.g., `day01.py`) corresponds to an input file of the same name (e.g., `inputs/day01.txt`).

If you'd like to run these solutions, you can replicate the input folder structure to match the examples above.

## Goals
- Practice Python programming.
- Tackle challenging and creative coding problems.
- Celebrate the holiday season with some coding fun!

Feel free to browse the solutions for inspiration or to compare approaches. 🎅✨
