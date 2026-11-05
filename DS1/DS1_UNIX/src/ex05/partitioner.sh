#!/bin/sh

INPUT="../ex03/hh_positions.csv"
HEADER=$(head -n 1 "$INPUT")

# Для каждой строки данных извлекаем дату и пишем в соответствующий файл
tail -n +2 "$INPUT" | while IFS= read -r line; do
    # Извлекаем дату из created_at (формат: 2025-10-06T...)
    date=$(echo "$line" | cut -d',' -f2 | cut -d'T' -f1)
    filename="${date}.csv"
    
    # Если файл новый — пишем заголовок
    if [ ! -f "$filename" ]; then
        echo "$HEADER" > "$filename"
    fi
    
    # Добавляем строку
    echo "$line" >> "$filename"
done
