def split_input():
    vetor = input().split(" ")
    return vetor[0], int(vetor[1]), int(vetor[2])

def jogar_corrida():
    nome_participante, qtd_propulsores, velocidade_propulsor = split_input()
    situacao_do_participante = input()
    desclassificado = False
    acabou = False
    qtd_propulsores_inicial = qtd_propulsores
    while situacao_do_participante != "Próximo" and not desclassificado and situacao_do_participante != "FIM":
        if situacao_do_participante == "Pit-Stop Espacial":
            qtd_propulsores += 1
        elif situacao_do_participante == "Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.":
            qtd_propulsores -= 1
            if qtd_propulsores <= 0:
                desclassificado = True
        elif situacao_do_participante == "Opa esse participante não está inscrito, desclassificando em 3, 2, 1...":
            desclassificado = True
        if not desclassificado:
            situacao_do_participante = input()
        if situacao_do_participante == "FIM":
            acabou = True

    if not desclassificado:
        velocidade_inicial  = qtd_propulsores_inicial * velocidade_propulsor
        velocidade_final = qtd_propulsores * velocidade_propulsor
        mensagem = f"--- Participante: {nome_participante} ---\nQtd de propulsores Final: {qtd_propulsores}\nVelocidade Inicial: {velocidade_inicial} km/h\nVelocidade Final: {velocidade_final} km/h"
        return mensagem, acabou, desclassificado
    elif desclassificado and qtd_propulsores <= 0:
        return f"BUUMM!! Infelizmente, {nome_participante} está fora da corrida.", acabou, desclassificado
    elif desclassificado and qtd_propulsores > 0:
        return f"O {nome_participante} achou que não descobriríamos, tirem {nome_participante} imediatamente da pista.", acabou, desclassificado


acabou = False
classificados = 0
desclassificados = 0
while not acabou:
    mensagem, acabou, desclassificado = jogar_corrida()
    print(mensagem)
    if desclassificado:
        desclassificados += 1
    else:
        classificados += 1

if classificados == 0:
    print("NÃO! Esses Droides me pagam, sabotaram minha corrida!")
else:
    print(f"Relatório da CIn Pod Race: {classificados} participantes terminaram a corrida e {desclassificados} foram desclassificados.")

