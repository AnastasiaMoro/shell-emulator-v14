"""Точка входа в эмулятор оболочки ОС."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import parse_args, print_config, validate_paths
from script_runner import run_script
from repl import run_repl


def main():
    """Запускает эмулятор оболочки."""
    args = parse_args()

    print_config(args.vfs_path, args.script)

    errors = validate_paths(args.vfs_path, args.script)
    if errors:
        for err in errors:
            print(f"Ошибка: {err}")

    if args.script:
        from commands import execute_command

        def output_func(text):
            print(text)

        success = run_script(
            args.script, execute_command, output_func
        )
        if not success:
            sys.exit(1)

    run_repl()


if __name__ == "__main__":
    main()