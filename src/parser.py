"""Парсер команд эмулятора с поддержкой переменных окружения."""
import os
import re


def expand_variables(text):
    """Раскрывает переменные окружения вида $VAR в тексте."""
    pattern = r'\$([A-Za-z_][A-Za-z0-9_]*)'

    def replace_var(match):
        """Заменяет переменную на её значение из окружения."""
        var_name = match.group(1)
        return os.getenv(var_name, match.group(0))

    return re.sub(pattern, replace_var, text)


def parse_command(command_line):
    """Разбирает строку на команду и аргументы."""
    expanded = expand_variables(command_line.strip())

    if not expanded:
        return None, []

    parts = expanded.split()
    cmd_name = parts[0]
    args = parts[1:]

    return cmd_name, args