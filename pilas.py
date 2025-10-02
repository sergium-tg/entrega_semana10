# -*- coding: utf-8 -*-
# Parte A — Pilas

# TODO 1: Validación de paréntesis con pila

def balanceado(exp):
    pila = []
    pares = {')':'(', ']':'[', '}':'{'}
    for caracter in exp:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    return not pila

# TODO 2: Conversión de decimal a binario usando pila
def decimal_a_binario(n):
    caracteres = []
    numeroBinario = ""
    if n == 0:
        return "0"
    while n > 0:
        binario = n % 2
        caracteres.append(binario)
        n = n //2
    while caracteres:
        numeroBinario += str(caracteres.pop())
    return numeroBinario

if __name__ == "__main__":
    print("== Pilas ==")
    print("Paréntesis balanceados:")
    print("1. La correctitud de la expresión (a+b)*[c-d] es: ")
    print(balanceado("(a+b)*[c-d]"))   # True
    print("2. La correctitud de la expresión (a+b*[c-d] es: ")
    print(balanceado("(a+b*[c-d]"))    # False
    print("3. Decimal a binario:")
    print(decimal_a_binario(13))  # 1101