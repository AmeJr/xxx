def eh_primo(n):
    """Retorna True se n for um número primo, False caso contrário."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n deve ser um número inteiro")
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    for numero in range(-1, 20):
        print(numero, eh_primo(numero))
