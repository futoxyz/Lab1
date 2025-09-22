def is_float(tok): # Проверка: является ли входящий токен "tok" числом. Возврат - True/False
    try:
        float(tok)
    except:
        return False
    return True
