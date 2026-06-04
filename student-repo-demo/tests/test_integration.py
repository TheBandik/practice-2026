"""Интеграционные тесты: полный цикл от файла до результата."""

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from algorithm import run
from utils import load_json, save_json


class TestEndToEnd:
    def test_sample_input_file(self):
        sample = Path(__file__).parent.parent / "data" / "sample_input.json"
        data = load_json(str(sample))
        result = run(data)
        assert result["sorted_items"] == sorted(data["items"])

    def test_expected_output_matches(self):
        sample = Path(__file__).parent.parent / "data" / "sample_input.json"
        expected_path = Path(__file__).parent.parent / "data" / "expected_output.json"
        data = load_json(str(sample))
        expected = load_json(str(expected_path))
        result = run(data)
        assert result["sorted_items"] == expected["sorted_items"]

    def test_save_and_load_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = str(Path(tmpdir) / "out.json")
            payload = {"items": [5, 3, 8, 1]}
            result = run(payload)
            save_json(out_path, result)
            loaded = load_json(out_path)
            assert loaded["sorted_items"] == result["sorted_items"]
