
def checar_se_eh_possivel_formar_filas(lista):
    maior_valor = max(lista)
    qtd_de_filas = lista.count(0)
    filas = []

    for _ in range(qtd_de_filas):
        filas.append([0])

    for i in range(1,maior_valor+1):
        if i in lista:
            qtd = lista.count(i)
            for fila in filas:
                if i-1 in fila:
                    if qtd > 0:
                        fila.append(i)
                        qtd -= 1

            if qtd > 0:
                return False
    return True


        

dicionario_de_numeros = {
    "Oooh look at him" : 0,
    "Baseball bat" : 1,
    "Aesthetic" : 2,
    "Fake Natty" : 3,
    "Chris Bumbstead, o CBUM" : 4,
    "Pope Francis" : 5,
    "O suco vicia" : 6,
    "I don't know you tell me" : 7,
    "Não é mesmo?" : 8,
    "Rodrigo Goes out" : 9,
}

resultados = {
    True : "YES",
    False : "NO"
}

n = int(input())

lista_pessoas_na_frente = []

for _ in range(n):
    frase = input()
    if "+" in frase:
        frase = frase.split("+")
    if isinstance(frase, list):
        for i in range(len(frase)):
            frase[i] = dicionario_de_numeros[frase[i]]
        num = 0

        for digit in frase:
            num = num * 10 + digit

        lista_pessoas_na_frente.append(num)
    else:
        lista_pessoas_na_frente.append(dicionario_de_numeros[frase])

print(resultados[checar_se_eh_possivel_formar_filas(lista_pessoas_na_frente)])