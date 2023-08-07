def calcula_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcula_fatorial(numero - 1)

def analisa_maiusculas_e_minusculas(string):
    maiusculas = 0
    minusculas = 0

    for char in string:
        if char.isupper():
            maiusculas += 1
        elif char.islower():
            minusculas += 1

    if maiusculas == minusculas:
        return 0
    
    return max([maiusculas, minusculas])

entrada = input()
quantidade = analisa_maiusculas_e_minusculas(entrada)

if quantidade == 0:
    preco = len(entrada) ** 2
else:
    preco = calcula_fatorial(quantidade) * len(entrada)


if preco >= 100:
    print(f"Hum... {preco}? Acho que na volta eu compro")
else:
    print(f"{preco}! Vou comprar todos!")