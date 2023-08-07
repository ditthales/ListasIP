def recebe_itens_da_sala():
    itens = input().split(" - ")
    return itens

def jornada(lista_de_salas, sala_atual, rupees = 0,tem_espada = False, resgatou_princesa = False):
    rupees += lista_de_salas[sala_atual].count('◇')
    if 'espada' in lista_de_salas[sala_atual]:
        tem_espada = True
    if 'Zelda' in lista_de_salas[sala_atual]:
        if 'Agahnim' in lista_de_salas[sala_atual]:
            if tem_espada:
                resgatou_princesa = True
        else:
            resgatou_princesa = True
    lista_de_salas[sala_atual].append("passei")
    for item in lista_de_salas[sala_atual]:
        if item.isdigit():
            sala_atual = int(item)
    if resgatou_princesa:
        return rupees, resgatou_princesa
    else:
        if "passei" in lista_de_salas[sala_atual]:
            return rupees, resgatou_princesa
        return jornada(lista_de_salas, sala_atual, rupees, tem_espada, resgatou_princesa)


qtd_salas = int(input())
lista_de_salas = []

for _ in range(qtd_salas):
    lista_de_salas.append(recebe_itens_da_sala())

sala_atual = int(input())

rupees, resgatou_princesa = jornada(lista_de_salas, sala_atual)

if resgatou_princesa:
    print(f"A princesa Zelda está a salvo e ainda conseguimos coletar {rupees} rupees")
else:
    print(f"Infelizmente a princesa ainda corre perigo, mas temos {rupees} rupees para nos ajudar nas buscas")
