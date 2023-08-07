n = int(input())

colecaoDeColecoes = []
notasDasColecoes = []

for n in range(0,n):
    colecao = input().split(", ")
    colecaoDeColecoes.append(colecao)
    notas = input().split(", ")
    for i in range(len(notas)):
        notas[i] = int(notas[i])
    notasDasColecoes.append(notas)

medias = []
for notas in notasDasColecoes:
    media = sum(notas)/len(notas)
    medias.append(media)

i = 0
for colecao in colecaoDeColecoes:
    status = True
    for item in colecao:
        if item == "colete preto" or item == "coturno":
            print(f"{item} é uma peça muito gótica, não faz o estilo da Glimmer.")
            status = False
            
            break
        elif item == "vestido com babados" or item == "blusa bufante":
            print(f"{item} é uma peça muito antiquada, infelizmente essa coleção não vai servir...")
            status = False
            
            break
    if status:
        if medias[i] < 6:
            print("Até que as peças são bonitinhas, mas não o bastante. Essa coleção não vai servir.")
        else:
            print("Que coleção linda! Com certeza vai ajudar Glimmer a se inspirar.")
    i+=1
        

