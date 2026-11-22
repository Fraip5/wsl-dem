#!/bin/bash

# Демонстрация interop - вызов Windows-программ из Linux

echo "========================================="
echo "Демонстрация 2: Interop с Windows"
echo "========================================="
echo ""

echo "Я работаю в Linux:"
uname -a
echo ""

echo "Открываю проводник Windows на текущей директории..."
cmd.exe /c explorer.exe . 2>/dev/null
echo "✓ Проводник открыт"
echo ""

echo "Список процессов Windows (первые 5):"
tasklist.exe 2>/dev/null | head -6
echo ""

echo "Открываю Notepad.exe..."
notepad.exe 2>/dev/null &
echo "✓ Notepad запущен"
echo ""

echo "Переменная PATH из Windows:"
cmd.exe /c "echo %PATH%" 2>/dev/null | head -1
echo ""

echo "========================================="
echo "Демонстрация завершена"
echo "========================================="
