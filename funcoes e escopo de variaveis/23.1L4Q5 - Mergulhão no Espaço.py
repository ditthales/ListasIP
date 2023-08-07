from math import floor
from operator import le
from re import S

def acha_vogais(string):
    vogais = "aeiou"
    contador = 0
    string = string.lower()
    for letra in string:
        if letra in vogais:
            contador += 1
    return contador

def acha_consoantes(string):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    contador = 0
    string = string.lower()
    for letra in string:
        if letra in consoantes:
            contador += 1
    return contador

def separa_numeros(string):
    string = string.lower()
    numeros = []
    numero_atual = ""
    for letra in string:
        if letra.isdigit():
            numero_atual += letra
        elif numero_atual:
            numeros.append(int(numero_atual))
            numero_atual = ""
    
    if numero_atual:
        numeros.append(int(numero_atual))

    return numeros

def sao_multiplos(string):
    numeros = separa_numeros(string)[::-1]
    if len(numeros) != 0:
        for passo in range(len(numeros) - 1):
            if numeros[passo] % numeros[-1] != 0:
                return False
        return True
    return False

def decodifica_coordenada(string):
    if not sao_multiplos(string):
        vogais = acha_vogais(string)
        consoantes = acha_consoantes(string)
        if consoantes != 0:
            divisao = vogais / consoantes
            piso = floor(divisao)
            componente = piso % 7
            return componente
        return 0
    return 3

def decodifica_codigos(string_X, string_Y):
    coordenada_X = decodifica_coordenada(string_X)
    coordenada_Y = decodifica_coordenada(string_Y)
    return coordenada_X, coordenada_Y

def monta_matriz(coordenada_X, coordenada_Y):
    componente_X = coordenada_X
    componente_Y = coordenada_Y * 7
    coordenada_geral = componente_X + componente_Y
    matriz = ""
    for index in range(7*7):
        if index == coordenada_geral:
            matriz += "☆ "
        else:
            matriz += ". "
        if (index + 1) % 7 == 0 and index != 49:
            matriz = matriz[:-1]
            matriz += "\n"
    matriz = matriz[:-1]
    return matriz

string_X = input()
string_Y = input()
coordenada_Y, coordenada_X = decodifica_codigos(string_X, string_Y)
matriz = monta_matriz(coordenada_X, coordenada_Y)
print(matriz)

if coordenada_X == 3 and coordenada_Y == 3:
    print("Ótimo, a estrela vai ficar exatamente no meio da fotografia! Posição melhor não existe!")
elif coordenada_X == 0 or coordenada_Y == 0 or coordenada_X == 6 or coordenada_Y == 6:
    print("Ihhh, vou ter que relocalizar a câmera, uma fotografia com a estrela na borda não dá! Infelizmente demora um pouco para criar outro código...")
else:
    print("Ok, agora é só enviar a matriz!")

if coordenada_X == 0 or coordenada_Y == 0 or coordenada_X == 6 or coordenada_Y == 6:
    print("Mesmo que eu não tenha conseguido uma matriz boa para tirar a foto, obrigado pelo seu tempo.")
else:
    print("Obrigado pela ajuda! A foto ficou ótima!")