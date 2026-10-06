"""Модуль конфигурации эмулятора оболочки."""
import argparse
import os
import sys


def parse_args():
    """Разбирает аргументы командной строки."""
    parser = argparse.ArgumentParser(
        description="Эмулятор оболочки UNIX"
    )
    parser.add_argument(
        "--vfs-path",
        type=str,
        default=None,
        help="Путь к физическому расположению VFS"
    )
    parser.add_argument(
        "--script",
        type=str,
        default=None,
        help="Путь к стартовому скрипту"
    )
    return parser.parse_args()


def print_config(vfs_path, script_path):
    """Выводит текущую конфигурацию эмулятора."""
    print("=== Конфигурация эмулятора ===")
    print(f"VFS путь: {vfs_path or 'не задан'}")
    print(f"Скрипт: {script_path or 'не задан'}")
    print("================================")


def validate_paths(vfs_path, script_path):
    """Проверяет существование указанных путей."""
    errors = []
    if vfs_path and not os.path.exists(vfs_path):
        errors.append(f"VFS путь не найден: {vfs_path}")
    if script_path and not os.path.exists(script_path):
        errors.append(f"Скрипт не найден: {script_path}")
    return errors