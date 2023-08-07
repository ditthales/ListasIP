# penteados = input().split(" - ")
# tops = input().split(" - ")
# bottoms = input().split(" - ")
# sapatos = input().split(" - ")

penteados = "solto de prancha - em coque - trançado".split(" - ")
tops = "cropped - vistido - sweater - blouse".split(" - ")
bottoms = "sweatpants - bell - shorts - brusa amarrada".split(" - ")
sapatos = "tênis - chinelinhos - sapatilha - scarpin - bota".split(" - ")

armario = [penteados, tops, bottoms, sapatos]

indexes = [0,0,0,0]

print("Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!")

decisao = "Acho que não combinou muito :/"
destaque = 0
k = 0

while decisao == "Acho que não combinou muito :/":
    # direcoes = input().split(" ")
    direcoes = "1< 1< 1> 2>".split(" ")

    print("Iniciando mesclagem...")

    for i in range(len(armario)):
        numero = direcoes[i].split("<")
        if len(numero) == 1:
            numero = direcoes[i].split(">")
        numero = int(numero[0])
        direcao = direcoes[i][1]
        meio = int(len(armario[i])/2)
        if k == 0:
            destaque = meio
        else:
            destaque = indexes[i]
        
        if direcao == ">":
            indexes[i] = int((meio + numero)%len(armario[i]))
        else:
            indexes[i] = int((meio - numero)%len(armario[i]))

    print("O look gerado foi:")
    print(f"cabelo {penteados[indexes[0]]}, {tops[indexes[1]]} com {bottoms[indexes[2]]} e {sapatos[indexes[3]]} nos pés.")

    decisao = input()
    k += 1

if decisao == "Amei!!":
    if tops[indexes[1]] == "camisa da seleção":
        print("Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!")
    else:
        print("Essa Barbie vai arrasar com o look perfeito!")
elif decisao == "Melhor escolher eu mesma":
    print("Acho que estou precisando de ajustes, Ken :(")

        
        