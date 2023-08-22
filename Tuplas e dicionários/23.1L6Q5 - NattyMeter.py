"""
infos{
    biceps: tamanho do biceps em cm
    tempo: tempo de treino diário em segundos
    frequencia: frenquencia na semana em dias
    gordura: % de gordura corporal
    suor: se o suspeito sua ou não
    natural: booleano que indica se o suspeito é natural ou não
}

"""

def adiciona_suspeito(nome):
    cadastro_de_suspeitos[nome] = {}

def atualiza_suspeito(nome, caracteristica, valor):
    cadastro_de_suspeitos[nome][caracteristica] = valor

def remove_suspeito(nome):
    if nome in cadastro_de_suspeitos:
        del cadastro_de_suspeitos[nome]
    else:
        print('Quem é esse crazy man? Não tá aqui na database')

def suspeito_eh_natural(nome):
    suspeitas = 0
    if "biceps" in cadastro_de_suspeitos[nome]:
        if cadastro_de_suspeitos[nome]["biceps"] > 45:
            suspeitas += 1
    if "tempo" in cadastro_de_suspeitos[nome]:
        if cadastro_de_suspeitos[nome]["tempo"] < 1800:
            suspeitas += 1
    if "frequencia" in cadastro_de_suspeitos[nome]:
        if cadastro_de_suspeitos[nome]["frequencia"] < 4:
            suspeitas += 1
    if "gordura" in cadastro_de_suspeitos[nome]:
        if cadastro_de_suspeitos[nome]["gordura"] < 10:
            suspeitas += 1
    if "suor" in cadastro_de_suspeitos[nome]:
        if not cadastro_de_suspeitos[nome]["suor"]:
            suspeitas += 1
    else:
        suspeitas += 1

    if suspeitas < 3:
        cadastro_de_suspeitos[nome]["natural"] = True
        return True
    cadastro_de_suspeitos[nome]["natural"] = False
    return False

def porcentagem_de_naturais():
    #comentar isso aqui caso sejam apenas os julgados até agora!
    # for nome in cadastro_de_suspeitos.keys():
    #     cadastro_de_suspeitos[nome]["natural"] = suspeito_eh_natural(nome)
    qtd_fake_natty = 0
    for nome in cadastro_de_suspeitos.keys():
        if "natural" in cadastro_de_suspeitos[nome]:
            if not cadastro_de_suspeitos[nome]["natural"]:
                qtd_fake_natty += 1

    porcentagem = qtd_fake_natty / len(cadastro_de_suspeitos) * 100
    porcentagem = round(porcentagem)
    return porcentagem

def desmembrar_caracteristicas(string):
    lista = string.split("->")

    lista[1] = lista[1].split(",")

    coisas_a_adicionar = {}

    for item in lista[1]:
        if "Biceps" in item:
            nova_lista = item.split(" ")
            tamanho = nova_lista[2][:-2]
            coisas_a_adicionar["biceps"] = int(tamanho)
        elif "Treino" in item:
            nova_lista = item.split(" ")
            if "minuto" in nova_lista[3]:
                coisas_a_adicionar["tempo"] = int(nova_lista[2]) * 60
            elif "hora" in nova_lista[3]:
                coisas_a_adicionar["tempo"] = int(nova_lista[2]) * 60 * 60
            else:
                coisas_a_adicionar["tempo"] = int(nova_lista[2])
        elif "Frequencia" in item:
            nova_lista = item.split(" ")
            coisas_a_adicionar["frequencia"] = int(nova_lista[2])
        elif "BF" in item:
            nova_lista = item.split(" ")
            porcentagem_gordura = nova_lista[2][:-1]
            coisas_a_adicionar["gordura"] = int(porcentagem_gordura)
        elif "Suor" in item:
            if "Seco" in item:
                coisas_a_adicionar["suor"] = False
            else:
                coisas_a_adicionar["suor"] = True
        
    return lista[0], coisas_a_adicionar

    
cadastro_de_suspeitos = {}

entrada = ""

while entrada != "FIM":
    entrada = input()
    #pronto
    if entrada == 'Adicionar suspeito':
        nome = input()
        adiciona_suspeito(nome)
        print(f'Novo suspeito: {nome}')
    elif entrada == 'Atualizar suspeito':
        caracteristicas = input()

        nome, coisas_a_adicionar = desmembrar_caracteristicas(caracteristicas)

        if nome in cadastro_de_suspeitos:
            for chave, valor in coisas_a_adicionar.items():
                cadastro_de_suspeitos[nome][chave] = valor
        else:
            print('Quem é esse crazy man? Não tá aqui na database')
    #pronto
    elif entrada == 'Remover suspeito':
        nome = input()
        remove_suspeito(nome)
        print(f'{nome} removido da lista de suspeitos, está limpo')
    #pronto
    elif entrada == 'Julgamento':
        nome = input()
        if nome in cadastro_de_suspeitos:
            natural = suspeito_eh_natural(nome)
            print(f'Eu já tenho o meu veredito, e o meu veredito, {nome}:')
            if natural:
                print("Natural")
            else:
                print('FAKE NATTY! USOU O SUCO!')
        else:
            print('Quem é esse crazy man? Não tá aqui na database')
    #pronto
    elif entrada == 'NattyMeter':
        print('NattyMeter, ON!')
        porcentagem = porcentagem_de_naturais()
        if porcentagem == 0:
            print('Oh yeah, vivemos em uma sociedade sem suco, um great day')
        else:
            print(f'NOOO! {porcentagem}% USARAM O SUCO')

    


