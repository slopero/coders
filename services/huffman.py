# huffman_service.py

import heapq
from typing import Dict, Optional

class Node:
    """
    Внутренний класс для представления узла дерева Хаффмана.
    """
    def __init__(self, char: Optional[str] = None, prob: float = 0.0, 
                 left: 'Optional[Node]' = None, right: 'Optional[Node]' = None):
        self.char = char      # Символ (только для листьев)
        self.prob = prob      # Вероятность/вес узла
        self.left = left      # Левый потомок
        self.right = right    # Правый потомок

    # Сравнение необходимо для работы очереди с приоритетом (heapq)
    def __lt__(self, other: 'Node') -> bool:
        return self.prob < other.prob

# Генерирует коды
def generate_codes(probabilities: Dict[str, float]) -> Dict[str, str]:
    if not probabilities:
        return {}

    # Краевой случай: один символ
    if len(probabilities) == 1:
        symbol = list(probabilities.keys())[0]
        return {symbol: '0'}

    # 1. Инициализация кучи листовыми узлами
    heap = [Node(char=char, prob=prob) for char, prob in probabilities.items()]
    heapq.heapify(heap)

    # 2. Построение дерева (жадный алгоритм)
    while len(heap) > 1:
        # Берем два узла с наименьшей вероятностью
        node_left = heapq.heappop(heap)
        node_right = heapq.heappop(heap)

        # Создаем новый внутренний узел
        merged_node = Node(
            char=None,
            prob=node_left.prob + node_right.prob,
            left=node_left,
            right=node_right
        )
        
        # Возвращаем в кучу
        heapq.heappush(heap, merged_node)

    root = heap[0]

    # 3. Обход дерева для генерации кодов
    codes = {}
    
    def _traverse(node: Optional[Node], current_code: str):
        if node is None:
            return
        
        # Если лист - сохраняем код
        if node.char is not None:
            codes[node.char] = current_code
            return

        # Рекурсия: лево -> '0', право -> '1'
        _traverse(node.left, current_code + '0')
        _traverse(node.right, current_code + '1')

    _traverse(root, '')
    codes = dict(sorted(codes.items(), key=lambda item: len(item[1])))
    return codes
