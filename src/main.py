#!/usr/bin/env python3

import random

from common import TOWERS_ALL, TOWERS_COMPLETED, \
        FIELD_SEP, LINE_SEP, \
        AREA_MARKER, COMMENT

from parser import Parser, parse_completed
from tower import Tower
from rules import *

def generate_pool() -> list[Tower]:
    pool = []

    parser = Parser(
        TOWERS_ALL,
        FIELD_SEP, LINE_SEP,
        AREA_MARKER, COMMENT
    )

    towers = parser.parse()
    print(f"Parsed {len(towers)} towers")

    completed = parse_completed(TOWERS_COMPLETED)
    print(f"Parsed {len(completed)} completed towers")

    print(
        "== Pool rules ==\n"
        + f"Areas:        {len(rule_areas)}\n"
        + f"Difficulties: {len(rule_difficulties)}\n"
        + f"Tower types:  {len(rule_types)}\n"
        + f"Completed?:   {rule_include_completed}\n"
        + "================"
    )

    for tower in towers:
        if rule_include_completed is False and tower.name in completed:
            continue

        if tower.area not in rule_areas:
            continue

        if tower.difficulty not in rule_difficulties:
            continue

        if tower.tower_type not in rule_types:
            continue

        pool.append(tower)

    print(f"Generated pool of size: {len(pool)}")
    return pool


def main() -> None:
    pool = generate_pool()

    if len(pool) < 1:
        print("Empty pool, can't select a tower")
        return

    print(f"Randomly selected tower: {random.choice(pool)}")

if __name__ == "__main__":
    try:
        main()


    except (EOFError, KeyboardInterrupt):
        pass
