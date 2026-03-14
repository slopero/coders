import math
from typing import Dict


def calculate_kraft_vector(codes: Dict[str, str]) -> float:
    return sum(2 ** (-len(code)) for code in codes.values() if code)


def calculate_average_code_length(probabilities: Dict[str, float], codes: Dict[str, str]) -> float:
    return sum(probabilities[symbol] * len(code) for symbol, code in codes.items())


def calculate_entropy(probabilities: Dict[str, float]) -> float:
    return -sum(p * math.log2(p) for p in probabilities.values() if p > 0)


def calculate_alphabet_redundancy(entropy: float, alphabet_size: int) -> float:
    if alphabet_size <= 1:
        return 0.0

    max_entropy = math.log2(alphabet_size)
    return (max_entropy - entropy) / max_entropy


def calculate_code_redundancy(entropy: float, average_code_length: float) -> float:
    if average_code_length == 0:
        return 0.0
    return (average_code_length - entropy) / average_code_length


def calculate_efficiency(entropy: float, average_code_length: float) -> float:
    if average_code_length == 0:
        return 0.0
    return entropy / average_code_length


def calculate_compression_ratio(code_redundancy: float) -> float:
    return 1 - code_redundancy


def calculate_all_metrics(probabilities: Dict[str, float], codes: Dict[str, str], alphabet_size: int) -> Dict[str, float]:
    q_avg = calculate_average_code_length(probabilities, codes)
    entropy = calculate_entropy(probabilities)
    r_code = calculate_code_redundancy(entropy, q_avg)

    return {
        "kraft_vector": calculate_kraft_vector(codes),
        "average_code_length": q_avg,
        "entropy": entropy,
        "alphabet_redundancy": calculate_alphabet_redundancy(entropy, alphabet_size),
        "code_redundancy": r_code,
        "efficiency": calculate_efficiency(entropy, q_avg),
        "compression_ratio": calculate_compression_ratio(r_code),
    }