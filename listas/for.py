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
    direcoes = "10< 1< 1> 2>".split(" ")

    print("Iniciando mesclagem...")

    for i in range(len(armario)):
        for item in direcoes[i]:
            
        numero = int(direcoes[i][0])
        direcao = direcoes[i][1]
        meio = int(len(armario[i])/2)
        if k == 0:
            destaque = meio
        else:
            destaque = indexes[i]
        
        if direcao == ">":
            indexes[i] = int((destaque + numero)%len(armario[i]))
        else:
            indexes[i] = int((destaque - numero)%len(armario[i]))
    decisao = ""

print(indexes)
    

        
        