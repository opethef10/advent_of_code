import argparse
from pathlib import Path

FILE_PATH = Path(__file__)
MAIN_DIR = FILE_PATH.parent
INPUTS_DIR = MAIN_DIR / "inputs"
EXAMPLE_INPUTS_DIR = MAIN_DIR / "example_inputs"

def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments for the script."""

    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--example', action='store_true', help='Run the script with the example input instead of the true input')

    return parser.parse_args()

def input_path(path_str) -> Path:
    args = parse_arguments()
    path = Path(path_str)
    file_stem = path.stem
    input_path = INPUTS_DIR / f"{file_stem}.txt"
    example_input_path = EXAMPLE_INPUTS_DIR / f"{file_stem}.txt"

    return input_path if not args.example else example_input_path

def input_lines(path_str) -> str:
    path = input_path(path_str)
    with path.open() as file:
        lines = file.readlines()
    return lines

def input_text(path_str) -> str:
    path = input_path(path_str)
    return path.read_text()
