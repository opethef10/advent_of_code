import importlib
from pathlib import Path

MAIN_DIR = Path(__file__).parent


def get_module(year: int, day: int):
    module_name = f"year{year}.day{day:02d}"
    return importlib.import_module(module_name)


def input_path(year: int, day: int, example: bool = False) -> Path:
    year_dir = MAIN_DIR / f"year{year}"
    file_stem = f"day{day:02d}"
    input_folder_name = "example_inputs" if example else "inputs"
    return year_dir / input_folder_name / f"{file_stem}.txt"


def input_lines(path: Path) -> list[str]:
    with path.open() as file:
        lines = file.readlines()
    return lines


def input_text(path: Path) -> str:
    return path.read_text()
