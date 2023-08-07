comando = ""
listaDeAraras = []
listaDeAssuntos = []
i = 0
falouTudo = True
itensNaoFalados = [[]]

while comando != "Meninas, acho que já falei demais. Vamos para o shopping?":
    listaDeAraras.append(input().split(", "))
    listaDeAssuntos.append(input().split(", "))
    print(f"Arara {i}:")
    if len(listaDeAraras[i]) != len(listaDeAssuntos[i]):
        print("Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!")

    for item in listaDeAssuntos[i]:
        if item not in listaDeAraras[i]:
            falouTudo = False
    
    for item in listaDeAraras[i]:
        if item not in listaDeAssuntos[i]:
            itensNaoFalados[i].append(item)

    if len(itensNaoFalados[i]) != 0:
        profissoes = ", ".join(itensNaoFalados[i])
        print(f"Poxa, Barbie! Você acabou desorganizando essa arara, e {len(itensNaoFalados[i])} profissões vão ficar de fora da conversa. São elas: {profissoes}.")


    if falouTudo:
        print("Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!")

    
    itensNaoFalados.append([])
    comando = input()
    i+=1