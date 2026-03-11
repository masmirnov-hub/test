# injection_tests.py
# SQL injection
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")

# Path traversal
open(f"/var/data/{user_input}", 'r')

# Log injection
logging.info(f"User action: {user_input}")  # Пользователь может вставить перевод строки

# Command injection
os.system(f"ping {host}")  # Пользователь может добавить ; rm -rf /
