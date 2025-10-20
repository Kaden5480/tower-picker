import math
import re

from tower import Area, Difficulty, Tower

class Parser:
    filename: str
    field_sep: str
    line_sep: str
    area_marker: str
    comment: str

    current_area: Area | None

    def __init__(
        self,
        filename: str,
        field_sep: str,
        line_sep: str,
        area_marker: str,
        comment: str
    ) -> None:
        self.filename = filename
        self.field_sep = field_sep
        self.line_sep = line_sep
        self.area_marker = area_marker
        self.comment = comment

    def parse_tower(self, line: str) -> Tower | None:
        info = line.split(self.field_sep)

        if len(info) < 3:
            print(f"WARNING: {info} has less than 3 fields")
            return None

        name_full = info[0]
        name = info[1]

        try:
            difficulty = Difficulty(math.floor(float(info[2])))

        except ValueError:
            print(f"WARNING: difficulty '{info[2]}' should be a float")
            return None

        return Tower(name, name_full, difficulty, self.current_area)

    def parse(self) -> list[Tower]:
        towers = []

        with open(self.filename, "r", encoding="utf-8") as f:
            data = f.read()

        lines = data.split(self.line_sep)

        for line in lines:
            line = line.strip()

            if len(line) < 1:
                continue

            if line.startswith(self.comment):
                continue

            if line.startswith(self.area_marker):
                line = re.sub(self.area_marker, "", line, count=1) \
                        .strip()

                try:
                    self.current_area = Area(line)

                except ValueError:
                    print(f"Skipping invalid area: {line}")
                    self.current_area = None

                continue

            if self.current_area is None:
                continue

            tower = self.parse_tower(line)
            if tower is not None:
                towers.append(tower)

        return towers

# Separate function for parsing completed towers
def parse_completed(filename: str) -> list[str]:
    with open(filename, "r") as f:
        lines = filter(
            lambda line: line.startswith("-") is False and len(line) > 0,
            map(lambda line: re.sub("\\s+", " ", line).strip(), f.readlines())
        )

        return list(map(lambda line: line.split()[1], lines))

