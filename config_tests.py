# config_tests.py
# Debug mode
DEBUG = True          # Режим отладки включен
SECRET_KEY = "dev"    # Простой ключ разработки

# SSL issues
requests.get(url, verify=False)  # Проверка SSL отключена

# CORS misconfiguration
CORS_ALLOWED_ORIGINS = ["*"]      # Разрешены все сайты
CORS_ALLOW_CREDENTIALS = True     # Можно передавать куки

# Weak TLS
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Старая версия TLS
