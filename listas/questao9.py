import string


n = int(input())
m = int(input())

stringM = []
numM = []

subListNum = []
subListString = []
temSoma = False

for i in range(0,m):
    entrada = input()
    entrada = entrada.split(' ')
    stringM.append(entrada[0])
    numM.append(int(entrada[1]))

for i in range(len(numM)):
    for j in range(i+1, len(numM)+1):
        sublistaNum = numM[i:j]
        sublistaString = stringM[i:j]
        soma = sum(sublistaNum)
        if soma == n:
            subListNum = sublistaNum
            subListString = sublistaString
            temSoma = True

if temSoma:
    posicoes = ""
    for item in subListString:
        posicoes += f"{item} "
    posicoes = posicoes[:-1]
    mensagem = f"Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {posicoes}!"
    print(mensagem)
else:
    print("Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima")

