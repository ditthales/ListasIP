mtrz = [["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"]]


voceY = 3
voceX = 0
cambistaY = 7
cambistaX = 0
pipocaY = 0
pipocaX = 0
barbieY = 0
barbieX = 7
oppenheimerY = 7
oppenheimerX = 7

cambistaPegou = False
assistiBarbie = False
assistiOppenheimer = False
cambistaPipoca = False


# voceY = int(input())
# voceX = int(input())
# cambistaY = int(input())
# cambistaX = int(input())
# pipocaY = int(input())
# pipocaX = int(input())
# barbieY = int(input())
# barbieX = int(input())
# oppenheimerY = int(input())
# oppenheimerX = int(input())

while (cambistaX != voceX or cambistaY != voceY) and (voceX != barbieX or voceY != barbieY) and (voceX != oppenheimerX or voceY != oppenheimerY):
    
    matriz = [["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"]]

    direcao = input()

    if cambistaX > voceX:
        if cambistaX != 0:
            cambistaX -= 1
    elif cambistaX < voceX:
        if cambistaX != 7:
            cambistaX += 1
    else:
        if cambistaY > voceY:
            if cambistaY != 0:
                cambistaY -= 1
        elif cambistaY < voceY:
            if cambistaY != 7:
                cambistaY += 1

    if cambistaX == voceX and cambistaY == voceY:
        cambistaPegou = True
    
    if pipocaX != -2 and pipocaY != -2:
        if direcao == 'esquerda':
            if voceX != 0:
                voceX -= 1
        elif direcao == 'direita':
            if voceX != 7:
                voceX += 1
        elif direcao == 'cima':
            if voceY != 0:
                voceY -= 1
        elif direcao == 'baixo':
            if voceY != 7:
                voceY += 1

    if cambistaX == voceX and cambistaY == voceY:
        cambistaPegou = True

    if voceX == pipocaX and voceY == pipocaY:
        pipocaX = -1
        pipocaY = -1
    
    if cambistaX == pipocaX and cambistaY == pipocaY:
        cambistaPipoca = True

    for y in range(0,8):
        for x in range(0,8):
            if not cambistaPipoca:
                if x == pipocaX and y == pipocaY:
                    matriz[x][y] = "P"
            if x == barbieX and y == barbieY:
                matriz[x][y] = "B"
            if x == oppenheimerX and y == oppenheimerY:
                matriz[x][y] = "O"
            if not cambistaPegou:
                if x == voceX and y == voceY:
                    matriz[x][y] = "V"
            if x == cambistaX and y == cambistaY:
                matriz[x][y] = "C"

    matrizString = ""
    for y in range(0,8):
        if y != 0:
            matrizString += "\n"
        for x in range(0,8):
            if x != 7:
                matrizString += f"{matriz[x][y]} "
            else:
                matrizString += f"{matriz[x][y]}"

    print(matrizString)

    distancia = (voceX - cambistaX)**2 + (voceY - cambistaY)**2

    if cambistaPegou:
        break

    if voceX == barbieX and voceY == barbieY:
        assistiBarbie = True
        break
    elif voceX == oppenheimerX and voceY == oppenheimerY:
        assistiOppenheimer = True
        break

    if pipocaX == -1 and pipocaY == -1:
        print('Finalmente! Peguei a pipoca')
        pipocaX -= 1
        pipocaY -= 1
    elif pipocaX < -1 and pipocaY < -1:
        print('Já peguei a pipoca')
        pipocaX -= 1
        pipocaY -= 1
    else:
        print('Ainda não achei a pipoca')

    if distancia <= 9:
        print('Preciso acelerar, o cambista tá na minha cola!\n')
    elif distancia > 16:
        print('O cambista está longe, mas não posso ficar parado\n')
    else:
        print('Consigo ver lá longe o cambista, mas é melhor acelerar!\n')
    
if pipocaX >= 0 and pipocaY >= 0 and (assistiBarbie or assistiOppenheimer):
    print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')
elif pipocaX < 0 and pipocaY < 0 and assistiBarbie:
    print('A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?')
elif pipocaX < 0 and pipocaY < 0 and assistiOppenheimer:
    print('Aí sim, que filmaço! Christopher Nolan nunca erra!')
elif cambistaPegou:
    print('Droga! Agora volto pra casa sem filme e sem dinheiro.')
    
