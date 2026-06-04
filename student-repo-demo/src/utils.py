"""Вспомогательные функции: ввод/вывод, валидация данных."""

import json
from pathlib import Path


def load_json(path: str) -> dict:
    """Загружает JSON-файл и возвращает словарь."""
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    with file.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, data: dict) -> None:
    """Сохраняет словарь в JSON-файл."""
    file = Path(path)
    file.parent.mkdir(parents=True, exist_ok=True)
    with file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
