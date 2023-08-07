entrada = input().split(" ; ")

n = int(entrada[0])
valor = int(entrada[1])

listaDeItens = []
custos = []
valorDisponivel = valor
i = 0
acao = ""

while i <= n and acao != "Fim! Muito obrigada pela ajuda!!":
    acao = input()
    if acao == "Quero adicionar um item":
        entrada = input()
        objeto = entrada.split(" - ")[0]
        filme = entrada.split(" - ")[1].split(" , ")[0]
        custo = int(entrada.split(" - ")[1].split(" , ")[1])
        custos.append(custo)

        if len(listaDeItens) < n and valorDisponivel >= custos[-1]:
            append = f"{objeto} - {filme}"
            listaDeItens.append(append)
            valorDisponivel = valor - sum(custos)
            print(f"Vá em frente, Ken! Você ainda tem {valorDisponivel} barbieCoins disponíveis")
        else:
            custos.pop()
            print('Avise a Barbie que isso não será possível.')
            valorDisponivel = valor - sum(custos)

    elif acao == "Quero remover um item":
        objeto = input()
        i = 0
        entrou = False
        for item in listaDeItens:
            entrou = True
            if objeto in item:
                custos.pop(i)
                listaDeItens.pop(i)
                print("Ok, Barbie!")
                valorDisponivel = valor - sum(custos)
                print(f"Ken, você ainda tem {valorDisponivel} barbieCoins disponíveis")
            else:

                if i == len(listaDeItens) - 1:
                    print("Barbie, infelizmente não consegui fazer isso.")
            i += 1
        if len(listaDeItens) == 0 and entrou == False:
            print("Barbie, infelizmente não consegui fazer isso.")


    elif acao == "Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?":
        if len(listaDeItens) != 0:
            print("Claro!")
            print("\n".join(listaDeItens))
        else:
            print("Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!")
    elif acao == "Fim! Muito obrigada pela ajuda!!":
        print("Por nada! Estou sempre à disposição!")
        

