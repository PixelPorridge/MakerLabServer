# Package Imports
from enum import Enum


# Champions
class Champion(Enum):
    KNIGHT = 0
    WIZARD = 1
    ROGUE = 2
    ARCHER = 3


# Stats
class Stat(Enum):
    STRENGTH = 0
    DEFENCE = 1
    SPEED = 2
    DEXTERITY = 3
    VITALITY = 4
    WISDOM = 5


# Champion Stats
championStats = ((3, 4, 1, 2, 4, 1),  # Knight
                 (4, 1, 2, 1, 2, 4),  # Wizard
                 (2, 2, 4, 4, 2, 1),  # Rogue
                 (3, 2, 3, 3, 2, 2))  # Archer
