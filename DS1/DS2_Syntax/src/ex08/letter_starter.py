import sys


def generate_letter(email: str) -> None:
    found = False
    name = ''
    
    with open('employees.tsv', 'r', encoding='utf-8') as f:
        next(f)
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 3 and parts[2] == email:
                name = parts[0]
                found = True
                break
    
    if found:
        print(f'{name}, добро пожаловать в нашу команду! Мы уверены, что работать вместе с тобой будет очень приятно. Для нас это важно - мы стремимся, чтобы в компании работали именно такие люди.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    
    generate_letter(sys.argv[1])
