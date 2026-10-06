"""Графический интерфейс эмулятора оболочки."""
import os
import socket
import sys
import tkinter as tk
from tkinter import scrolledtext

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from parser import parse_command
from commands import execute_command


def get_window_title():
    """Формирует заголовок окна из данных ОС."""
    user = os.getenv("USER", "user")
    host = socket.gethostname()
    return f"Эмулятор-[{user}@{host}]"


def create_gui():
    """Создаёт и настраивает главное окно эмулятора."""
    root = tk.Tk()
    root.title(get_window_title())
    root.geometry("800x600")

    output_area = scrolledtext.ScrolledText(
        root, wrap=tk.WORD, state=tk.DISABLED
    )
    output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    input_frame = tk.Frame(root)
    input_frame.pack(fill=tk.X, padx=10, pady=10)

    prompt_label = tk.Label(input_frame, text="$ ")
    prompt_label.pack(side=tk.LEFT)

    input_entry = tk.Entry(input_frame, width=70)
    input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    input_entry.focus()

    def on_enter(event):
        """Обрабатывает нажатие Enter в поле ввода."""
        command_line = input_entry.get()
        input_entry.delete(0, tk.END)

        append_output(output_area, f"$ {command_line}\n")

        if not command_line.strip():
            return

        cmd_name, args = parse_command(command_line)

        if cmd_name is None:
            append_output(output_area, "Ошибка: пустая команда\n")
            return

        if cmd_name == "exit":
            root.destroy()
            return

        result = execute_command(cmd_name, args)
        append_output(output_area, f"{result}\n")

    input_entry.bind("<Return>", on_enter)

    root.mainloop()


def append_output(text_widget, text):
    """Добавляет текст в область вывода."""
    text_widget.config(state=tk.NORMAL)
    text_widget.insert(tk.END, text)
    text_widget.config(state=tk.DISABLED)
    text_widget.see(tk.END)