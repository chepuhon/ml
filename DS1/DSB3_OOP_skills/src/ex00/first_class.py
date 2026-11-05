class Must_Read:
    """Класс для чтения и печати CSV файла"""
    
    # Чтение файла и печать внутри тела класса
    file = open('data.csv', 'r')
    content = file.read()
    print(content)
    file.close()


if __name__ == '__main__':
    # Создание экземпляра класса запускает код в теле класса
    try:
        instance = Must_Read()
    except Exception as e:
        print(f"Ошибка: {e}")
