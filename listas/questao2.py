itensDaLista = input().split(", ")
itensEncontrados = input().split(", ")

itensEncontradosDaLista = []
itensNaoEncontrados = []

for item in itensDaLista:
    if item in itensEncontrados:
        itensEncontradosDaLista.append(item)
    else:
        itensNaoEncontrados.append(item)

if not itensEncontradosDaLista:
    print(f"Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {len(itensDaLista)} itens em casa.")
else:
    print("Esses são os itens que já tenho em casa:")
    n = 1
    for item in itensEncontradosDaLista:
        print(f"{n}º item: {item}")
        n+=1
    if not itensNaoEncontrados:
        print(f"Que ótimo, consegui encontrar cada um dos {len(itensDaLista)} itens!")
    else:
        print(f"Irei precisar comprar {len(itensNaoEncontrados)} itens antes do meu encontro!")


print("Isso é tudo! Hora de me preparar!")

