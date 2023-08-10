from turtle import pos


def printar_tabuleiro():
    for i in range(len(tabuleiro)):
        print(tabuleiro[i],end="")
        if (i + 1) % offset == 0 and i != 0:
            print("")
    print("-----------------------")

def realizar_queda_posicao(pos):
    if pos < offset:
        tabuleiro[pos] = "O"
        return 0
    
    tabuleiro[pos + offset] = tabuleiro[pos]
    tabuleiro[pos] = tabuleiro[pos - offset]
    return realizar_queda_posicao(pos - offset)
    

    
    

offset = 3
# tabuleiro = ["O","O","O","O","O","O",
#             "O","X","O","O","O","O",
#             "O","X","O","O","O","O",
#             "O","O","O","O","O","O",
#             "O","O","O","O","O","O",
#             "O","O","O","O","O","O"]

tabuleiro = ["O","H","O",
            "O","O","O",
            "O","H","O"]

printar_tabuleiro()

posicao = 4
while tabuleiro[posicao] == "O":
    realizar_queda_posicao(posicao)
    printar_tabuleiro()


