def processar_colunas(matriz):
    for linha in matriz:
        linha[0] = linha[0]*(linha[0]+1)
    return matriz

# Exemplo de uso
matriz_original = [
    [2, 5],
    [3, 4]
]

nova_matriz = processar_colunas(matriz_original)

for linha in nova_matriz:
    print(linha)