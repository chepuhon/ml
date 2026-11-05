import sys
import os


class Research:
    """Класс для чтения и валидации CSV файла"""
    
    def __init__(self, filepath):
        """Конструктор, принимающий путь к файлу"""
        self.filepath = filepath
    
    def file_reader(self):
        """Метод для чтения и возврата содержимого файла с валидацией"""
        # Проверяем существование файла
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Файл '{self.filepath}' не найден")
        
        # Читаем файл
        with open(self.filepath, 'r') as file:
            content = file.read()
        
        # Валидируем структуру файла
        self._validate_csv(content)
        
        return content
    
    def _validate_csv(self, content):
        """Проверка структуры CSV файла"""
        lines = content.strip().split('\n')
        
        # Проверяем, что есть хотя бы заголовок
        if len(lines) < 1:
            raise ValueError("Файл пуст или не содержит заголовка")
        
        # Проверяем заголовок (должен содержать две колонки, разделённые запятой)
        header = lines[0].strip()
        if ',' not in header:
            raise ValueError("Заголовок должен содержать две колонки, разделённые запятой")
        
        header_parts = header.split(',')
        if len(header_parts) != 2:
            raise ValueError("Заголовок должен содержать ровно две колонки")
        
        # Проверяем данные (начиная со второй строки)
        for i, line in enumerate(lines[1:], start=2):
            line = line.strip()
            if not line:  # Пропускаем пустые строки
                continue
            
            parts = line.split(',')
            
            # Проверяем количество колонок
            if len(parts) != 2:
                raise ValueError(f"Строка {i}: должна содержать ровно две колонки, разделённые запятой")
            
            # Проверяем значения (должны быть 0 или 1)
            val1, val2 = parts[0].strip(), parts[1].strip()
            
            if val1 not in ['0', '1']:
                raise ValueError(f"Строка {i}: первое значение должно быть 0 или 1, получено '{val1}'")
            
            if val2 not in ['0', '1']:
                raise ValueError(f"Строка {i}: второе значение должно быть 0 или 1, получено '{val2}'")
            
            # Проверяем, что значения разные (не 0,0 и не 1,1)
            if val1 == val2:
                raise ValueError(f"Строка {i}: значения должны быть разными (не может быть 0,0 или 1,1)")


if __name__ == '__main__':
    try:
        # Проверяем наличие аргумента командной строки
        if len(sys.argv) != 2:
            print("Использование: python3 first_constructor.py <путь_к_файлу>")
            sys.exit(1)
        
        # Получаем путь к файлу из аргументов
        filepath = sys.argv[1]
        
        # Создаём экземпляр класса с путём к файлу
        research = Research(filepath)
        
        # Читаем и печатаем содержимое
        content = research.file_reader()
        print(content)
        
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        sys.exit(1)
