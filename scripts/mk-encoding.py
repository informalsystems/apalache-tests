#!/usr/bin/env python3

"""
Generates files for the array encoding experiments. It is intended to
used from the project Makefile.
"""

import argparse
import csv
import sys

from argparse import Namespace
from pathlib import Path


def generate_params(args: Namespace) -> None:
    print("params", args.strategy)


# Mazimize size of experiments to measure
# reflected in set cardinality
MAX_EXPERIMENT_SIZE = 15
EXPERIMENT_CARDINALITIES = list(range(0, MAX_EXPERIMENT_SIZE + 1, 2))

CONSTANT_MODULE_FMT = """
------------------- MODULE Constants -----------------------
\* NOTE: This file is automatically generated. See the project Makefile
EXTENDS Naturals

CONSTANT
  \\* @type: Set(Int);
  Values

{cinit_ops}

============================================================
"""

CSV_HEADER = ["no", "filename", "tool", "timeout", "init", "inv", "next", "args"]


def generate_constants() -> None:
    """
    Generate CInitN operators for the Constants.tla file, one for each N in
    `EXPERIMENT_CARDINALITIES`
    """
    cinit_ops = "\n".join(
        f"CInit{n} == Values = 0..{n}" for n in EXPERIMENT_CARDINALITIES
    )
    print(CONSTANT_MODULE_FMT.format(cinit_ops=cinit_ops))


def csv_row(index: int, size: int, path: Path, encoding: str):
    return [
        str(index),
        str(path),
        "apalache",
        "20m",
        "Init",
        "Inv",
        "Next",
        f"--smt-encoding={encoding} --length={size} --cinit=CInit{size}",
    ]


def spec_name_of_strategy_path(strat: Path) -> Path:
    strategy, *_ = strat.name.split("-")
    _, name = strategy.split("+")  # Remove the strategy prefix
    return Path("array-encoding", name).with_suffix(".tla")


def generate_csv(path: Path) -> None:
    """
    Generate CSV content for
    """
    # Experiment file name, relative to performance directory
    exp_path = spec_name_of_strategy_path(path)
    n_exps = len(EXPERIMENT_CARDINALITIES)
    # Sequence of tripples
    idx_size_encoding = zip(
        range(1, n_exps * 2 + 1),
        EXPERIMENT_CARDINALITIES * 2,
        (["arrays"] * n_exps) + (["oopsla19"] * n_exps),
    )
    exps = [CSV_HEADER] + [
        csv_row(idx, size, exp_path, encoding)
        for idx, size, encoding in idx_size_encoding
    ]
    csv.writer(sys.stdout).writerows(exps)


def generate_file_content(path: Path) -> None:
    if path.name == "Constants.tla":
        return generate_constants()
    elif path.suffix == ".csv":
        return generate_csv(path)
    else:
        raise RuntimeError(f"Unsupported generation path: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate param files for the array encoding benchmarks"
    )
    parser.add_argument("file", help="File to generate", type=Path)

    args = parser.parse_args()
    generate_file_content(Path.cwd() / args.file)


if __name__ == "__main__":
    main()
