class Research:
    """Класс для чтения CSV файла"""
    
    def file_reader(self):
        """Метод для чтения и возврата содержимого файла"""
        file = open('data.csv', 'r')
        content = file.read()
        file.close()
        return content


if __name__ == '__main__':
    try:
        # Создаём экземпляр класса
        research = Research()
        
        # Вызываем метод и печатаем результат
        result = research.file_reader()
        print(result)
        
    except FileNotFoundError:
        print("Ошибка: файл data.csv не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
