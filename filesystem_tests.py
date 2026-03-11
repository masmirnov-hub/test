# filesystem_tests.py
# Insecure temp file
open("/tmp/data.txt", "w")  # Временный файл в предсказуемом месте

# Symlink vulnerability
if os.path.exists(path):    # Проверяем существование
    os.remove(path)         # Удаляем
with open(path, "w") as f:   # Создаем новый
    f.write(data)            # Проблема: между проверкой и записью файл могли подменить

# Wrong permissions
os.chmod("config.ini", 0o644)  # Файл могут читать все пользователи
open("private.key", "r")       # Приватный ключ в открытом доступе
