# auth_tests.py
# JWT issues
jwt.encode({"admin": True}, "secret", algorithm="none")  # Без подписи

# Session fixation
session['user_id'] = request.args.get('session_id')  # Берем сессию из URL

# Weak password policy
if len(password) < 6:  # Минимальная длина 6 символов
    return "Too short"

# No rate limiting
def login(username, password):  # Можно перебирать пароли бесконечно
    return check_password(username, password)
