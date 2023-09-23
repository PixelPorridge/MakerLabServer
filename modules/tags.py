# Package Imports
from enum import Enum

# File Imports
from modules.champions import *
from modules.spells import *


# Constants
NULL_TERMINATOR = "~"
STRING_LENGTH = 20
NUMBER_LENGTH = 8


# Tag Type (Champion/Spell)
class TagType(Enum):
    CHAMPION = 0
    SPELL = 1


# Champion Tag Addresses
class ChampionAddress(Enum):
    STRING = 0

    TYPE = 5
    CHAMPION = 6

    LEVEL = 7
    EXP = 8

    STRENGTH = 9
    DEFENCE = 10
    SPEED = 11
    DEXTERITY = 12
    VITALITY = 13
    WISDOM = 14


# Spell Tag Addresses
class SpellAddress(Enum):
    TYPE = 0
    SPELL = 1


# Encode Champion
def encode_champion():
    pass


# Decode Champion
def decode_champion():
    pass


# Encode Spell
def encode_spell():
    pass


# Decode Spell
def decode_spell():
    pass
