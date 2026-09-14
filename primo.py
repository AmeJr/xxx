def eh_primo(n):
    """Retorna True se n for um número primo, False caso contrário."""
    if n <= 1:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    for numero in range(-1, 20):
        print(numero, eh_primo(numero))
