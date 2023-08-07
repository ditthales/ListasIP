def somar_numeros(numero1, numero2) -> float:
    resultado = numero1 + numero2
    return resultado

def subtrair_numeros(numero1, numero2) -> float:
    resultado = numero1 - numero2
    return resultado

def multiplicar_numeros(numero1, numero2) -> float:
    resultado = numero1 * numero2
    return resultado

def dividir_numeros(numero1, numero2) -> float:
    resultado = numero1 / numero2
    return resultado

def exp_numeros(numero1, numero2) -> float:
    resultado = numero1 ** numero2
    return resultado

def decidir_acao(string, numero1, numero2) -> float:
    if string == "Quero somar esses dois números:":
        resultado = somar_numeros(numero1, numero2)
    elif string == "Preciso subtrair um pelo outro":
        resultado = subtrair_numeros(numero1, numero2)
    elif string == "Quanto dá o produto disso?":
        resultado = multiplicar_numeros(numero1, numero2)
    elif string == "Vou dividir aqui rapidinho":
        resultado = dividir_numeros(numero1, numero2)
    elif string == "E se eu elevar um pelo outro?":
        resultado = exp_numeros(numero1, numero2)
    else:
        resultado = 0

    return resultado

quantidade_de_operacoes = int(input())

for operacao in range(1, quantidade_de_operacoes + 1):
    string = input()
    numero1 = float(input())
    numero2 = float(input())
    resultado = decidir_acao(string, numero1, numero2)
    print("O resultado da {}ª operação foi {:.1f}".format(operacao, resultado))

if quantidade_de_operacoes != 0:
    print("Ufa, já deu de cálculos por hoje!")
else:
    print("Vou relaxar aqui na minha nave")
