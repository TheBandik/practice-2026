"""Алгоритмическое ядро.

Замените содержимое этого модуля реализацией вашего варианта.
Пример ниже: сортировка слиянием с подсчётом числа сравнений.
"""


def merge_sort(arr: list) -> tuple[list, int]:
    """Сортировка слиянием; возвращает (отсортированный список, число сравнений)."""
    if len(arr) <= 1:
        return arr[:], 0

    mid = len(arr) // 2
    left, lc = merge_sort(arr[:mid])
    right, rc = merge_sort(arr[mid:])
    merged, mc = _merge(left, right)
    return merged, lc + rc + mc


def _merge(left: list, right: list) -> tuple[list, int]:
    result, i, j, comparisons = [], 0, 0, 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, comparisons


def run(data: dict) -> dict:
    """Основная точка входа алгоритма.

    Args:
        data: словарь с ключом "items" — список чисел для сортировки.

    Returns:
        словарь с "sorted_items" и "comparisons".
    """
    items = data.get("items", [])
    sorted_items, comparisons = merge_sort(items)
    return {
        "sorted_items": sorted_items,
        "comparisons": comparisons,
    }
