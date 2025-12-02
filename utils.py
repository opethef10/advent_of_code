import importlib
from pathlib import Path


def get_module(year: int, day: int):
    module_name = f"year{year}.day{day:02d}"
    return importlib.import_module(module_name)


def input_path(year: int, day: int, example: bool = False) -> Path:
    path = Path(f"year{year}/day{day:02d}.py")
    file_stem = path.stem
    parent_dir = path.parent
    input_folder_name = "example_inputs" if example else "inputs"
    return parent_dir / input_folder_name / f"{file_stem}.txt"


def input_lines(path: Path) -> list[str]:
    with path.open() as file:
        lines = file.readlines()
    return lines


def input_text(path: Path) -> str:
    return path.read_text()
