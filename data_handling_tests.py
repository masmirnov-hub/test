# data_handling_tests.py
# Weak random
token = random.randint(0, 1000)  # Случайное число от 0 до 1000

# No constant-time comparison
if token == user_token:  # Сравнение строк
    grant_access()

# Hardcoded salt
SALT = "fixed_salt"  # Одна соль для всех паролей

# Plaintext passwords
passwords = {"user": "pass123"}  # Хранение в открытом виде
