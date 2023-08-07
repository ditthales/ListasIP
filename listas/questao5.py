n = int(input())

matriz = [[]]

for andar in range(n):
    for comodo in range(n):
        matriz[andar].append(input())
    matriz.append([])

matriz.pop()

matrizString = ""

for i in range(n):
    mensagem = " ".join(matriz[i])
    matrizString += mensagem
    if i != n - 1:
        matrizString += "\n"


print(matrizString)
