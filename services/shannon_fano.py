def shannon_fano(probabilities: dict) -> dict:
    codes = {letter: '' for letter in probabilities}

    def _split(symbols: list):
        if len(symbols) <= 1:
            return

        total = sum(probabilities[s] for s in symbols)
        best_diff = float('inf')
        best_split = 1

        left_sum = 0
        for i in range(len(symbols) - 1):
            left_sum += probabilities[symbols[i]]
            right_sum = total - left_sum
            diff = abs(left_sum - right_sum)
            if diff <= best_diff:
                best_diff = diff
                best_split = i + 1

        left = symbols[:best_split]
        right = symbols[best_split:]

        for s in left:
            codes[s] += '0'
        for s in right:
            codes[s] += '1'

        _split(left)
        _split(right)

    _split(list(probabilities.keys()))
    return codes
