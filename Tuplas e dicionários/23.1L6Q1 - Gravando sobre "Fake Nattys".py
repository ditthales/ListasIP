
def receber_inputs(n):
    dicionario = {}
    for _ in range(n):
        entrada = input().split(" - ")
        nome = entrada[0]
        resto = entrada[1].split(" ")
        profissao = resto[0]
        avaliacao = resto[1]
        mes = int(resto[2])
        dicionario[nome] = (profissao, avaliacao, mes)

    return dicionario

def procurar_fake_nattys(dicionario, mes):
    chaves = []
    for chave, valor in dicionario.items():
        if mes in valor and "fake" in valor:
            chaves.append(chave)
    return chaves


n = int(input())
dicionario = receber_inputs(n)
mes_procurado = int(input())

chaves = procurar_fake_nattys(dicionario, mes_procurado).sort()

if len(chaves) != 0:
    print("Os fake nattys do mês são:")
    for chave in chaves:
        print(f"{chave} - {dicionario[chave][0]}")
else:
    print("Até agora não temos ninguém pra expor na internet neste mês :(")

