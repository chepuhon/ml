#!/bin/sh

OUTPUT="hh_positions_restored.csv"

# Берём заголовок из оригинального файла (ex03)
HEADER=$(head -n 1 ../ex03/hh_positions.csv)
echo "$HEADER" > "$OUTPUT"

# Объединяем все файлы с датами, пропуская ИХ заголовки
for file in *.csv; do
    # Пропускаем сам результат и служебные файлы
    case "$file" in
        hh_positions_restored.csv|hh_positions.csv) continue ;;
    esac
    # Пропускаем заголовок каждого файла-партиции и добавляем данные
    tail -n +2 "$file" >> "$OUTPUT"
done

# Сортируем результат как в ex03: по created_at, затем по id
TEMP=$(mktemp)
head -n 1 "$OUTPUT" > "$TEMP"
tail -n +2 "$OUTPUT" | sort -t',' -k2,2 -k1,1n >> "$TEMP"
mv "$TEMP" "$OUTPUT"
