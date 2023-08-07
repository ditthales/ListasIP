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


tabuleiro = receber_tabuleiro()
print(checar_vitoria('x'))

