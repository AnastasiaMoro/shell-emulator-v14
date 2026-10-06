"""Модуль выполнения стартовых скриптов."""
import os


def run_script(script_path, execute_func, output_func):
    """
    Выполняет стартовый скрипт построчно.

    Останавливается при первой ошибке.
    Отображает ввод и вывод, имитируя диалог.

    :param script_path: путь к скрипту
    :param execute_func: функция выполнения команды
    :param output_func: функция вывода текста
    :return: True если скрипт выполнен успешно
    """
    if not os.path.exists(script_path):
        output_func(f"Ошибка: скрипт не найден: {script_path}")
        return False

    with open(script_path, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            output_func(f"$ {line}")

            cmd_name, args = _parse_simple(line)

            if cmd_name is None:
                continue

            result = execute_func(cmd_name, args)

            if result.startswith("Ошибка"):
                output_func(result)
                output_func(
                    f"Скрипт остановлен на строке {line_num}"
                )
                return False

            if result:
                output_func(result)

    return True


def _parse_simple(line):
    """Простой парсер для скрипта."""
    parts = line.split()
    if not parts:
        return None, []
    return parts[0], parts[1:]