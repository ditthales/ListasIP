def criar_trigramas(string):
    string = string.lower()
    trigramas = []

    for i in range(len(string) - 2):
        trigrama = string[i:i+3]
        trigramas.append(trigrama)

    return trigramas

entrada = ""
arquivo = []
trigramas = {}

while entrada != "END_OF_FILE":
    entrada = input()
    arquivo.append(entrada.lower())

for i in range(len(arquivo)):
    trigramas[i] = criar_trigramas(arquivo[i])

n = int(input())
buscas = []

for _ in range(n):
    buscas.append(input().lower())

linhas_a_buscar = [[]]

for i in range(len(buscas)):
    for chave, valor in trigramas.items():
        if buscas[i][:3] in valor:
            linhas_a_buscar[i].append(chave)
    linhas_a_buscar.append([])
linhas_a_buscar.pop()

achados = []

for i in range(len(buscas)):
    if len(linhas_a_buscar[i]) != 0:
        achou = False
        for j in range(len(linhas_a_buscar[i])):
            if buscas[i] in arquivo[linhas_a_buscar[i][j]]:
                achados.append(linhas_a_buscar[i][j])
                achou = True
                break
        if not achou:
            achados.append(-1)
            achou = False
    else:
        achados.append(-1)

for item in achados:
    print(item)
