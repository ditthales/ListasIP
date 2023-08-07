def recebe_inputs():
    entrada = input().split(" ")
    m = int(entrada[0])
    n = int(entrada[1])
    return m, n

def verifica_fibonacci(numero, a=0, b=1):
    if numero == a or numero == b:
        return True
    elif a + b > numero:
        return False
    else:
        return verifica_fibonacci(numero, b, a + b)

total_de_vidas, total_de_casas_inicial = recebe_inputs()
total_de_casas = total_de_casas_inicial

while total_de_vidas != 0 and total_de_casas != 0:
    numero_da_casa = int(input())
    if verifica_fibonacci(numero_da_casa):
        total_de_casas -= 1
    else:
        total_de_vidas -= 1
        print("Oh nao Link! Voce nao pode parar ainda, voce e a ultima esperanca de Hyrule!")
        total_de_casas = total_de_casas_inicial

if total_de_vidas > 0:
    print("Voce Adicionou A Master Sword ao seu inventario")
    print("Link Salve Hyrule!!!")
else:
    print("A ultima defesa de hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf")