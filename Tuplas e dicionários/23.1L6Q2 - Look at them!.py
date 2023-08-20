def receber_inputs(n):
    dicionario = {}
    for _ in range(n):
        entrada = input().split(" - ")
        nome = entrada[0]
        nota = int(entrada[1])
        categoria = entrada[2]
        dicionario[nome] = (nota, categoria)
    return dicionario

def ordenar_dicionario(dicionario):
    lista_de_nattys = []
    lista_de_fake_nattys = []
    for chave, valor in dicionario.items():
        if "natty" in valor:
            lista_de_nattys.append((chave, valor[0], valor[1]))
        else:
            lista_de_fake_nattys.append((chave, valor[0], valor[1]))
    lista_de_nattys_ordenada = sorted(lista_de_nattys, key=lambda x: x[1], reverse=True)
    lista_de_fake_nattys_ordenada = sorted(lista_de_fake_nattys, key=lambda x: x[1], reverse=True)
    return lista_de_nattys_ordenada, lista_de_fake_nattys_ordenada
    


n = int(input())
dicionario = receber_inputs(n)
nattys, fake_nattys = ordenar_dicionario(dicionario)

for item in nattys:
    print(f"{item[0]} - {item[1]} - {item[2]}")
for item in fake_nattys:
    print(f"{item[0]} - {item[1]} - {item[2]}")

