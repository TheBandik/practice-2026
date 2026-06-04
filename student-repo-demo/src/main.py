"""Точка входа. Разбирает аргументы CLI, вызывает алгоритм, выводит результат."""

import argparse
import json
import sys

from algorithm import run
from utils import load_json, save_json


def parse_args():
    parser = argparse.ArgumentParser(description="Описание вашего приложения")
    parser.add_argument("--input", default="data/sample_input.json",
                        help="Путь к файлу с входными данными")
    parser.add_argument("--output", default=None,
                        help="Путь к файлу результата (по умолчанию — stdout)")
    parser.add_argument("--verbose", action="store_true",
                        help="Подробный вывод")
    return parser.parse_args()


def main():
    args = parse_args()

    data = load_json(args.input)

    if args.verbose:
        print(f"Загружены данные: {data}", file=sys.stderr)

    result = run(data)

    if args.output:
        save_json(args.output, result)
        if args.verbose:
            print(f"Результат сохранён в {args.output}", file=sys.stderr)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
