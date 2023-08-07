# capsulas[1][0][0] -> segunda cápsula, primeiro astronauta, coordenada X
# capsulas -> astronautas -> astronauta

def calcular_distancia(x1, y1, x2, y2):
    distancia = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)
    return distancia

def checar_sobrevivencia(capsulas, posicao_explosao, raio_impacto):
    numero_de_sobreviventes = 0
    sobreviventes = [[]]
    index = 0
    for capsula in capsulas:
        if len(capsula) != 0:
            for astronauta in capsula:
                distancia = calcular_distancia(posicao_explosao[0], posicao_explosao[1], astronauta[0], astronauta[1])
                if distancia > raio_impacto:
                    numero_de_sobreviventes += 1
                    sobreviventes[index].append(astronauta)
            sobreviventes.append([])
        index += 1
    
    sobreviventes.pop()

    return numero_de_sobreviventes, sobreviventes

def achar_ponto_central(sobreviventes, numero_de_sobreviventes):
    x_sum = 0
    y_sum = 0
    ponto_central = []
    for capsula in sobreviventes:
        if len(capsula) != 0:
            x_sum = 0
            y_sum = 0
            for astronauta in capsula:
                x_sum += astronauta[0]
                y_sum += astronauta[1]
            ponto_central.append([x_sum/len(capsula), y_sum/len(capsula)])
    return ponto_central

def resgatar_astronautas(capsulas, posicao_explosao, raio_impacto):
    numero_de_sobreviventes, sobreviventes = checar_sobrevivencia(capsulas, posicao_explosao, raio_impacto)
    ponto_central = achar_ponto_central(sobreviventes, numero_de_sobreviventes)
    return numero_de_sobreviventes, ponto_central 

capsulas = eval(input())
posicao_explosao = eval(input())
raio_impacto = int(input())
# print(calcular_distancia(2,2,0,0))
numero_sobreviventes, sobreviventes = checar_sobrevivencia(capsulas, posicao_explosao, raio_impacto)
ponto_central = achar_ponto_central(sobreviventes, numero_sobreviventes)
array_unico = [numero_sobreviventes, ponto_central]
print(array_unico)

