import sys


def extract_names(input_file: str) -> None:
    with open(input_file, 'r', encoding='utf-8') as f:
        emails = f.read().strip().split('\n')
    
    with open('employees.tsv', 'w', encoding='utf-8') as out:
        out.write('Name\tSurname\tE-mail\n')
        for email in emails:
            email = email.strip()
            if not email:
                continue
            
            name_part = email.split('@')[0]
            name, surname = name_part.split('.')
            
            name_cap = name.capitalize()
            surname_cap = surname.capitalize()
            
            out.write(f'{name_cap}\t{surname_cap}\t{email}\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    
    extract_names(sys.argv[1])
    
