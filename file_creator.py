def create_empty_file(filename):
    """Створює пустий файл із заданим ім'ям."""
    try:
        with open(filename, 'w') as f:
            pass  # 'w' відкриває файл для запису, створюючи його, якщо він не існує
        print(f"Файл '{filename}' успішно створено.")
    except IOError as e:
        print(f"Помилка при створенні файлу '{filename}': {e}")

# Використання функції:
file_name = input(f"Введіть ім'я файлу \n")
create_empty_file(file_name)
