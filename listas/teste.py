direcoes = "10< 1< 1> 2>".split(" ")

for i in range(len(direcoes)):
    numero = direcoes[i].split("<")
    if len(numero) == 1:
        numero = direcoes[i].split(">")

    numero = int(numero[0])
    direcao = direcoes[i][1]
    print(numero)
    print(direcao)