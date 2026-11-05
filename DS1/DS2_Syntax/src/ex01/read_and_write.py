def convert_csv_to_tsv(input_file: str, output_file: str) -> None:
    with open(input_file, 'r', encoding='utf-8') as fin, \
         open(output_file, 'w', encoding='utf-8') as fout:
        for line in fin:
            line = line.rstrip('\n').rstrip('\r')
            if not line:
                continue

            fields = []
            current_field = []
            in_quotes = False
            i = 0
            n = len(line)

            while i < n:
                char = line[i]
                if in_quotes:
                    if char == '"':
                        if i + 1 < n and line[i + 1] == '"':
                            current_field.append('"')
                            i += 2
                            continue
                        in_quotes = False
                    else:
                        current_field.append(char)
                    i += 1
                else:
                    if char == '"':
                        in_quotes = True
                    elif char == ',':
                        fields.append(''.join(current_field))
                        current_field = []
                    else:
                        current_field.append(char)
                    i += 1

            fields.append(''.join(current_field))
            fout.write('\t'.join(fields) + '\n')


if __name__ == '__main__':
    convert_csv_to_tsv('ds.csv', 'ds.tsv')
