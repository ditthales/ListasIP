def gerar_variacoes(palavra):
    variacoes = []
    for letra in 'abcdefghijklmnopqrstuvwxyz':
        variacoes.append(palavra.replace('_', letra))
    return variacoes

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
    return palavas_mais_repetidas, contagem

def decidir_desempate(lista_de_palavras):
    
    menor_palavra = lista_de_palavras[0]
    for palavra in lista_de_palavras:
        if palavra < menor_palavra:
            menor_palavra = palavra
    
    return menor_palavra

n = int(input())

lista_de_variacoes = []
mais_repetidas = []

for _ in range(n):
    palavra = input()
    lista_de_variacoes.append(gerar_variacoes(palavra))


mais_repetidas, contagem = elementos_mais_repetidos(lista_de_variacoes)

palavra_final = decidir_desempate(mais_repetidas)

print(f"{palavra_final} {contagem[palavra_final]}")





