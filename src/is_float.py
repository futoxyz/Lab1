def is_float(tok):
    """
    Проверяет, является ли токен числом
    :param tok: Токен
    :return: True/False
    """
    try:
        float(tok)
    except:
        return False
    return True
