def decorador_mensaje(func):
    def wrapper(*args):
        result = func(*args)
        print("Se agregó un nuevo libro.")
        return result
    return wrapper