"""Юнит-тесты алгоритмического ядра."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from algorithm import merge_sort, run


class TestMergeSort:
    def test_sorted_result(self):
        result, _ = merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == sorted([3, 1, 4, 1, 5, 9, 2, 6])

    def test_empty_list(self):
        result, comparisons = merge_sort([])
        assert result == []
        assert comparisons == 0

    def test_single_element(self):
        result, comparisons = merge_sort([42])
        assert result == [42]
        assert comparisons == 0

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        result, _ = merge_sort(data)
        assert result == data

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        result, _ = merge_sort(data)
        assert result == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        data = [2, 2, 2, 1, 1]
        result, _ = merge_sort(data)
        assert result == sorted(data)

    def test_comparisons_positive(self):
        _, comparisons = merge_sort([3, 1, 2])
        assert comparisons > 0

    def test_does_not_modify_input(self):
        data = [3, 1, 2]
        original = data[:]
        merge_sort(data)
        assert data == original


class TestRun:
    def test_basic(self):
        result = run({"items": [3, 1, 2]})
        assert result["sorted_items"] == [1, 2, 3]
        assert "comparisons" in result

    def test_missing_key(self):
        result = run({})
        assert result["sorted_items"] == []

    def test_negative_numbers(self):
        result = run({"items": [-3, 0, -1, 2]})
        assert result["sorted_items"] == [-3, -1, 0, 2]
