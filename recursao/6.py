def receber_tabuleiro():
    tabuleiro = []
    for _ in range(3):
        entrada = input().split("|")
        for item in entrada:
            tabuleiro.append(item)
    i = 0
    tabuleiro_dict = {}
    for item in tabuleiro:
        tabuleiro_dict[i] = item
        i+=1
    return tabuleiro_dict

def space_is_free(n):
    if tabuleiro[n] == '_':
        return True
    return False

def is_board_empty():
    for v in tabuleiro.values():
        if v != "_":
            return False
    return True

def realizar_jogada(jogador, jogada):
    if space_is_free(jogada):
        tabuleiro[jogada] = jogador

def checar_vitoria(jogador):
    if (tabuleiro[0] == tabuleiro[1] and tabuleiro [0] == tabuleiro[2] and tabuleiro[0] == jogador):
        return True
    elif (tabuleiro[3] == tabuleiro[4] and tabuleiro [3] == tabuleiro[5] and tabuleiro[3] == jogador):
        return True
    elif (tabuleiro[6] == tabuleiro[7] and tabuleiro [6] == tabuleiro[8] and tabuleiro[6] == jogador):
        return True
    elif (tabuleiro[0] == tabuleiro[3] and tabuleiro [0] == tabuleiro[6] and tabuleiro[0] == jogador):
        return True
    elif (tabuleiro[1] == tabuleiro[4] and tabuleiro [1] == tabuleiro[7] and tabuleiro[1] == jogador):
        return True
    elif (tabuleiro[2] == tabuleiro[5] and tabuleiro [2] == tabuleiro[8] and tabuleiro[2] == jogador):
        return True
    elif (tabuleiro[0] == tabuleiro[4] and tabuleiro [0] == tabuleiro[8] and tabuleiro[0] == jogador):
        return True
    elif (tabuleiro[2] == tabuleiro[4] and tabuleiro [2] == tabuleiro[6] and tabuleiro[2] == jogador):
        return True 
    else:
        return False

def checar_empate():
    if '_' not in tabuleiro.values() and checar_vitoria('x') == False and checar_vitoria('o') == False:
        return True
    return False

def is_game_over():
    return checar_vitoria("x") or checar_vitoria("o") or checar_empate()

def jogada_X(tabuleiro):
    melhor_score = -1000
    melhor_jogada = 0

    for chave in tabuleiro.keys():
        if space_is_free(chave):
            tabuleiro[chave] = 'x'
            score = minimax(tabuleiro, False)
            tabuleiro[chave] = '_'
            if score > melhor_score:
                melhor_score = score
                melhor_jogada = chave

    realizar_jogada('x', melhor_jogada)
    return

def jogada_O(tabuleiro):
    melhor_score = 1000
    melhor_jogada = 0

    for chave in tabuleiro.keys():
        if space_is_free(chave):
            tabuleiro[chave] = 'o'
            score = minimax(tabuleiro, True)
            tabuleiro[chave] = '_'
            if score < melhor_score:
                melhor_score = score
                melhor_jogada = chave

    realizar_jogada('o', melhor_jogada)
    return
    
def minimax(tabuleiro, is_maximizing):

    if checar_vitoria('x'):
        return 100
    elif checar_vitoria('o'):
        return -100
    elif checar_empate():
        return 0

    if is_maximizing:
        melhor_score = -1000

        for chave in tabuleiro.keys():
            if space_is_free(chave):
                tabuleiro[chave] = 'x'
                score = minimax(tabuleiro, False)
                tabuleiro[chave] = '_'
                if score > melhor_score:
                    melhor_score = score
        
        return melhor_score
    else:
        melhor_score = 800

        for chave in tabuleiro.keys():
            if space_is_free(chave):
                tabuleiro[chave] = 'o'
                score = minimax(tabuleiro, True)
                tabuleiro[chave] = '_'
                if score < melhor_score:
                    melhor_score = score
        
        return melhor_score

def print_tabuleiro():
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print(f'--+---+--')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print(f'--+---+--')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')
    print(f'--+---+--')
    print('---------------------------------------------')

tabuleiro = receber_tabuleiro()

ganhou = [False, False, False]

while not is_game_over():
    if is_board_empty():
        realizar_jogada("x", 0)
    else:
        jogada_X(tabuleiro)
    print_tabuleiro()
    if not is_game_over():
        jogada_O(tabuleiro)
        print_tabuleiro()

if is_game_over():
    ganhou[0] = checar_vitoria("x")
    ganhou[1] = checar_vitoria("o")
    ganhou[2] = checar_empate()

if ganhou[0]:
    print("As previsões indicam que o resultado é vitória do x. Aperte o botão correspondente")
elif ganhou[1]:
    print("As previsões indicam que o resultado é vitória do o. Aperte o botão correspondente")
elif ganhou[2]:
    print("As previsões indicam que o resultado é empate. Aperte o botão correspondente")    
