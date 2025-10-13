import math
from enum import Enum

class TowerType(Enum):
    #MiniTower = 0
    Steeple   = 1
    Tower     = 2
    Citadel   = 3


class Difficulty(Enum):
    Easy         = 1
    Medium       = 2
    Hard         = 3
    Difficult    = 4
    Challenging  = 5
    Intense      = 6
    Remorseless  = 7
    Insane       = 8
    Extreme      = 9
    Terrifying   = 10
    Catastrophic = 11


class Area(Enum):
    Ring0  = "Purgatorio"
    Ring1  = "Ring 1"
    Ring2  = "Ring 2"
    Ring3  = "Ring 3"
    Ring4  = "Ring 4"
    Ring5  = "Ring 5"
    Ring6  = "Ring 6"
    Ring7  = "Ring 7"
    Ring8  = "Ring 8"
    Ring9  = "Ring 9"

    Zone1  = "Zone 1"
    Zone2  = "Zone 2"
    Zone3  = "Zone 3"
    Zone4  = "Zone 4"
    Zone5  = "Zone 5"
    Zone6  = "Zone 6"
    Zone7  = "Zone 7"
    Zone8  = "Zone 8"
    Zone9  = "Zone 9"
    Zone10 = "Zone 10"

    Ring1B = "Forgotten Ridge"
    Ring2B = "Garden of Eeshöl"
    Ring4B = "Silent Abyss"
    Ring5B = "Lost River"
    Ring6B = "Ashen Towerworks"
    Ring8B = "The Starlit Archives"
    Zone1B = "Steelspire Horizon"
    Zone2B = "Arcane Area"
    Zone3B = "Paradise Atoll"


class Tower:
    name: str
    name_full: str
    tower_type: TowerType
    difficulty: Difficulty
    area: Area

    def __init__(
        self,
        name: str,
        name_full: str,
        difficulty: Difficulty,
        area: Area
    ) -> None:
        self.name = name
        self.name_full = name_full
        self.difficulty = difficulty
        self.area = area

        # Infer tower type
        lower_name = self.name_full.lower()

        if lower_name.startswith("steeple"):
            self.tower_type = TowerType.Steeple
        elif lower_name.startswith("tower") or self.name == "TT":
            self.tower_type = TowerType.Tower
        elif lower_name.startswith("citadel"):
            self.tower_type = TowerType.Citadel
        else:
            print(f"Unknown tower type for: '{self.name_full}'")
            self.tower_type = TowerType.Tower

    def __repr__(self) -> str:
        return f"[{self.area.value}] {self.name} ({self.name_full}) <{self.tower_type.name}|{self.difficulty.name}>"
