n = int(input())
nomeCriaturas = []
nomeCriaturasSemRepeticao = []

for i in range(0,n):
    nomeCriaturas.append(input())

for elemento in nomeCriaturas:
    if elemento not in nomeCriaturasSemRepeticao:
        nomeCriaturasSemRepeticao.append(elemento)
    else:
        print("Criatura repetida")

for elemento in nomeCriaturasSemRepeticao:
    print(elemento)