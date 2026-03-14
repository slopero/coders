from services.count_char import count_char
from services.count_chance import count_ch
from services.shannon_fano import shannon_fano
from services.huffman import generate_codes
from services.read_text import read_pdf
from services.metrics import calculate_all_metrics
from config import SYMBOL


def _print_metrics(title: str, metrics: dict):
    print(f"\nКоличественные характеристики ({title}):")
    print(f"Вектор Крафта: {metrics['kraft_vector']:.6f}")
    print(f"Средняя длина кодового слова: {metrics['average_code_length']:.6f}")
    print(f"Энтропия: {metrics['entropy']:.6f}")
    print(f"Избыточность алфавита: {metrics['alphabet_redundancy']:.6f}")
    print(f"Избыточность кода: {metrics['code_redundancy']:.6f}")
    print(f"Коэффициент эффективности: {metrics['efficiency']:.6f}")
    print(f"Коэффициент сжатия: {metrics['compression_ratio']:.6f}")

def calculate(path:str):
    text = read_pdf(path)
    if text is None:
        return

    count = 0
    letters = count_char(text)
    letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))
    print("Количество каждой буквы в тексте:")
    for key, value in letters.items():
        print(f"{key} = {value}")
        count += value
    print(f"Всего букв: {count}\n")
    chance = count_ch(letters, count)
    count_chance = 0
    for key, value in chance.items():
        print(f"{key} = {value:.6f}")
        count_chance += value
    print(f"Сумма вероятностей: {count_chance:.6f}")

    codes_sh_f = shannon_fano(chance)
    print("\nКоды Шеннона-Фано:")
    for key, value in codes_sh_f.items():
        print(f"{key} = {value}")

    metrics_sh_f = calculate_all_metrics(chance, codes_sh_f, len(SYMBOL))
    _print_metrics("Шеннон-Фано", metrics_sh_f)

    codes_huff = generate_codes(chance)
    print("\nКоды Хаффмана")
    for key, value in codes_huff.items():
        print(f"{key} = {value}")

    metrics_huff = calculate_all_metrics(chance, codes_huff, len(SYMBOL))
    _print_metrics("Хаффман", metrics_huff)