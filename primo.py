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
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


if __name__ == "__main__":
    for numero in range(-1, 20):
        print(numero, eh_primo(numero))
