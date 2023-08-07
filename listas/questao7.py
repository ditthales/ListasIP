profissao_prevista = input()
profissao_do_dia = input()

itens_medica = ["Estetoscopio", "Esfigmomanometro", "Jaleco", "Caneta" , "Celular"]
itens_inform = ["Calculadora", "Oculos", "Notebook", "Camisa Social", "Caderno"]
itens_padeira = ["Rolo", "Caneta", "Avental", "Colher de Pau", "Caderno"]
itens_economista = ["Calculadora", "Caneta", "Camisa Social", "Agenda", "Celular"]
itens_maromba = ["Halter", "Agenda", "Celular", "Legging", "Corda"]

bolsa = []

if profissao_prevista == "Medica":
    bolsa = itens_medica.copy()
elif profissao_prevista == "Assistente de Informatica":
    bolsa = itens_inform.copy()
elif profissao_prevista == "Padeira":
    bolsa = itens_padeira.copy()
elif profissao_prevista == "Economista":
    bolsa = itens_economista.copy()
elif profissao_prevista == "Personal Trainer":
    bolsa = itens_maromba.copy()

bolsa_desejada = []

if profissao_do_dia == "Medica":
    bolsa_desejada = itens_medica.copy()
elif profissao_do_dia == "Assistente de Informatica":
    bolsa_desejada = itens_inform.copy()
elif profissao_do_dia == "Padeira":
    bolsa_desejada = itens_padeira.copy()
elif profissao_do_dia == "Economista":
    bolsa_desejada = itens_economista.copy()
elif profissao_do_dia == "Personal Trainer":
    bolsa_desejada = itens_maromba.copy()

acao = input()

while acao != "Sair":
    if acao == "Adicionar":
        item = input()
        if item in bolsa:
            print(f"Barbie, você já colocou {item} na bolsa")
        elif item in bolsa_desejada:
            print(f"{item} adicionado à bolsa")
            bolsa.append(item)
        elif item not in bolsa_desejada:
            print(f"Barbie, {item} não esta na lista de itens de {profissao_do_dia}")

    elif acao == "Retirar":
        item = input()
        if item not in bolsa:
            print(f"Barbie, como você vai retirar algo que já não esta ai?")
        elif item not in bolsa_desejada:
            print(f"{item} retirado da bolsa")
            bolsa.remove(item)
        elif item in bolsa_desejada:
            print(f"Não faca isso Barbie, você precisa de {item} para trabalhar de {profissao_do_dia}")
        
    acao = input()

bolsa_alfabetica = sorted(bolsa)

mensagem = "Itens na bolsa: " + ", ".join(bolsa_alfabetica)

print(mensagem)

esqueceu_algo = False

item_esquecido = ""

for item in bolsa_desejada:
    if item not in bolsa:
        item_esquecido = item

item_errado = ""

for item in bolsa:
    if item not in bolsa_desejada:
        item_errado = item



if bolsa_alfabetica == sorted(bolsa_desejada):
    print("Boa Barbie, foi na correria mas tudo deu certo!")
elif item_esquecido != "":
    print(f"Oh não!! Barbie, você esqueceu de pegar {item_esquecido}!!")
elif item_errado != "":
    print(f"Barbie, você esqueceu de tirar {item_errado}, você não usa ele trabalhando de {profissao_do_dia}")
