# Constants
TYPE_BYTE = 0


# Tag (Champion/Spell)
class Tag():
    CHAMPION = 0
    SPELL = 1


# Champion Tag Bytes
class ChampionByte():
    CHAMPION = 1

    LEVEL = 2
    EXP = 3

    STRENGTH = 4
    DEFENCE = 5
    SPEED = 6
    DEXTERITY = 7
    VITALITY = 8
    WISDOM = 9


# Spell Tag Bytes
class SpellByte():
    SPELL = 1


# Encode Champion
def encode_champion(champion: int,
                    level: list[int, int],
                    stats: list[int, int, int, int, int, int]) -> str:
    code = ""

    code += _encode_number(Tag.CHAMPION)
    code += _encode_number(champion)

    code += _encode_number(level[0])
    code += _encode_number(level[1])

    code += _encode_number(stats[0])
    code += _encode_number(stats[1])
    code += _encode_number(stats[2])
    code += _encode_number(stats[3])
    code += _encode_number(stats[4])
    code += _encode_number(stats[5])

    return code


# Decode Champion
def decode_champion(code: str) -> dict:
    data = {"type": 0,
            "champion": 0,
            "level": [0, 0],
            "stats": [0, 0, 0, 0, 0, 0]}

    data["type"] = _decode_byte(code[TYPE_BYTE])
    data["champion"] = _decode_byte(code[ChampionByte.CHAMPION])

    data["level"][0] = _decode_byte(code[ChampionByte.LEVEL])
    data["level"][1] = _decode_byte(code[ChampionByte.EXP])

    data["stats"][0] = _decode_byte(code[ChampionByte.STRENGTH])
    data["stats"][1] = _decode_byte(code[ChampionByte.DEFENCE])
    data["stats"][2] = _decode_byte(code[ChampionByte.SPEED])
    data["stats"][3] = _decode_byte(code[ChampionByte.DEXTERITY])
    data["stats"][4] = _decode_byte(code[ChampionByte.VITALITY])
    data["stats"][5] = _decode_byte(code[ChampionByte.WISDOM])

    return data


# Encode Spell
def encode_spell(spell: int) -> str:
    code = ""

    code += _encode_number(Tag.SPELL)
    code += _encode_number(spell)

    return code


# Decode Spell
def decode_spell(code: str) -> dict:
    data = {"type": 0,
            "spell": 0}

    data["type"] = _decode_byte(code[TYPE_BYTE])
    data["spell"] = _decode_byte(code[SpellByte.SPELL])

    return data


# Decode Type
def decode_type(code: str) -> int:
    return _decode_byte(code[TYPE_BYTE])


# Encode Number
def _encode_number(number: int) -> str:
    return chr(number)


# Decode Byte
def _decode_byte(byte: str) -> int:
    return ord(byte)
