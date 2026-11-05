#!/bin/sh

INPUT="../ex02/hh_sorted.csv"
OUTPUT="hh_positions.csv"

# 1. Копируем заголовок без изменений
head -n 1 "$INPUT" > "$OUTPUT"

# 2. Обрабатываем каждую строку данных
tail -n +2 "$INPUT" | while IFS= read -r line; do
    # Извлекаем содержимое 3-го поля (name) между кавычками
    # Регулярка захватывает текст внутри третьих кавычек, игнорируя запятые внутри названия
    name=$(echo "$line" | sed -E 's/^"[^"]*","[^"]*","([^"]*)".*$/\1/')
    
    new_pos="-"
    found=""
    
    # Проверяем наличие ключевых слов (порядок: Junior -> Middle -> Senior)
    echo "$name" | grep -q "Junior" && found="${found}Junior/"
    echo "$name" | grep -q "Middle" && found="${found}Middle/"
    echo "$name" | grep -q "Senior" && found="${found}Senior/"
    
    # Если нашли хоть один уровень, формируем результат и убираем лишний слэш в конце
    if [ -n "$found" ]; then
        new_pos=$(echo "$found" | sed 's/\/$//')
    fi
    
    # Собираем строку обратно:
    # prefix: "id","date","
    # new_pos: найденный уровень
    # suffix: ",has_test,"url"
    prefix=$(echo "$line" | sed -E 's/^("[^"]*","[^"]*",").*$/\1/')
    suffix=$(echo "$line" | sed -E 's/^"[^"]*","[^"]*","[^"]*"(.*)$/\1/')
    
    echo "${prefix}${new_pos}${suffix}" >> "$OUTPUT"
done
