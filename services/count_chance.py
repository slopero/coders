def count_ch(letters: dict, count: int) -> dict:
    chance = {}
    for key, value in letters.items():
        chance[key] = value / count
    return chance