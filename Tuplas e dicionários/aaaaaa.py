def elementos_mais_repetidos(lista_de_listas):
    contagem = {}
    for lista in lista_de_listas:
        for elemento in lista:
            if elemento in contagem:
                contagem[elemento] += 1
            else:
                contagem[elemento] = 1

    mais_repeticoes = max(contagem.values())
    palavas_mais_repetidas = []
    for chave, valor in contagem.items():
        if valor == mais_repeticoes:
            palavas_mais_repetidas.append(chave)
    return palavas_mais_repetidas


# Exemplo de uso
lista_de_listas = [[0,1,2,3],[0,2,4,6],[1,3,5,7],[0,1,10,20,30]]
resultados = elementos_mais_repetidos(lista_de_listas)
print(resultados)