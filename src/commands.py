"""Команды эмулятора оболочки (заглушки для Этапа 1)."""


def execute_command(cmd_name, args):
    """Выполняет команду и возвращает результат."""
    commands = {
        "ls": cmd_ls,
        "cd": cmd_cd,
    }

    if cmd_name not in commands:
        return f"Ошибка: неизвестная команда '{cmd_name}'"

    return commands[cmd_name](args)


def cmd_ls(args):
    """Заглушка команды ls."""
    return f"ls: {args}"


def cmd_cd(args):
    """Заглушка команды cd."""
    if not args:
        return "cd: отсутствует аргумент"
    return f"cd: {args}"