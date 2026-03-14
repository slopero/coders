from config import SYMBOL
def count_char(text: str) -> dict:
    letters = {}
    for letter in text:
        if letter in letters:
            continue
        else:
            if letter in SYMBOL:
                letters[f"{letter}"] = text.count(letter) 
    return letters