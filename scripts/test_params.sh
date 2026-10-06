#!/bin/bash
# Тест параметров командной строки эмулятора

echo "=== Тест 1: Запуск без параметров ==="
/opt/homebrew/bin/python3.11 src/main.py &
sleep 2
kill %1 2>/dev/null

echo ""
echo "=== Тест 2: Запуск с путём к VFS ==="
/opt/homebrew/bin/python3.11 src/main.py --vfs-path /tmp/vfs_test &
sleep 2
kill %1 2>/dev/null

echo ""
echo "=== Тест 3: Запуск со скриптом ==="
/opt/homebrew/bin/python3.11 src/main.py --script scripts/demo.sh &
sleep 3
kill %1 2>/dev/null

echo ""
echo "=== Тест 4: Запуск с несуществующим скриптом ==="
/opt/homebrew/bin/python3.11 src/main.py --script scripts/nonexistent.sh

echo ""
echo "=== Все тесты завершены ==="