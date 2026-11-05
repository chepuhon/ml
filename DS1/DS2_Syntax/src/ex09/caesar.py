import sys


def caesar_cipher(text: str, shift: int, operation: str) -> str:
    result = []
    
    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
                if operation == 'encode':
                    new_char = chr((ord(char) - base + shift) % 26 + base)
                else:
                    new_char = chr((ord(char) - base - shift) % 26 + base)
            elif char.isupper():
                base = ord('A')
                if operation == 'encode':
                    new_char = chr((ord(char) - base + shift) % 26 + base)
                else:
                    new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)


def main() -> None:
    if len(sys.argv) != 4:
        raise Exception("Invalid number of arguments")
    
    operation = sys.argv[1]
    text = sys.argv[2]
    
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer")
    
    if operation not in ['encode', 'decode']:
        raise Exception("Invalid operation")
    
    for char in text:
        if '\u0400' <= char <= '\u04FF':
            raise Exception("The script does not support your language yet.")
    
    result = caesar_cipher(text, shift, operation)
    print(result)


if __name__ == '__main__':
    main()
