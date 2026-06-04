# [Название проекта] — учебная ознакомительная практика 2026

**Студент:** Фамилия Имя Отчество  
**Группа:** БИ-##-##  
**Вариант:** А-## / Б-## — *краткое название варианта*  
**Язык:** Python 3.12

## Описание

Краткое описание задачи и реализованного алгоритма (2–4 предложения).

## Структура репозитория

```
.
├── src/
│   ├── main.py          # точка входа, CLI
│   ├── algorithm.py     # алгоритмическое ядро
│   └── utils.py         # вспомогательные функции (ввод/вывод, валидация)
├── tests/
│   ├── test_algorithm.py    # юнит-тесты алгоритма
│   └── test_integration.py  # интеграционные тесты
├── data/
│   ├── sample_input.json    # пример входных данных
│   └── expected_output.json # ожидаемый результат для тестов
├── Dockerfile
├── .gitignore
└── README.md
```

## Установка и запуск

### Локально

```bash
# 1. Клонировать репозиторий
git clone https://github.com/<username>/<repo>.git
cd <repo>

# 2. Установить зависимости
pip install -r requirements.txt   # если есть внешние зависимости

# 3. Запустить
python src/main.py --input data/sample_input.json
```

### В Docker

```bash
# Собрать образ
docker build -t practice-app .

# Запустить
docker run --rm practice-app --input data/sample_input.json

# Запустить с внешним файлом данных
docker run --rm -v "$(pwd)/data:/app/data" practice-app --input /app/data/sample_input.json
```

## Параметры запуска

| Параметр | Описание | По умолчанию |
|----------|----------|--------------|
| `--input` | Путь к файлу с входными данными | `data/sample_input.json` |
| `--output` | Путь к файлу результата | stdout |
| `--verbose` | Подробный вывод | выключен |

## Запуск тестов

```bash
python -m pytest tests/ -v
```

## Зависимости

- Python ≥ 3.10
- *список библиотек при наличии*
