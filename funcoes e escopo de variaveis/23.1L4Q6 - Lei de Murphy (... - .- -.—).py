def eh_numero_perfeito(number):
    if number == 0:
        return False
    divisores = []
    decrementador = number - 1
    while decrementador > 0:
        if number % decrementador == 0:
            divisores.append(decrementador)
        decrementador -= 1
    if sum(divisores) == number:
        return True
    return False

def resolve_expressao(expressao):
    pilha = []
    operadores = {'+', '-', '*', '/'}

    for token in expressao.split():
        if token.isdigit() or (token[1:].isdigit() and token[0] == '-'):
            pilha.append(int(token))  # Trata números positivos e negativos
        elif token in operadores:
            valor2 = pilha.pop()
            valor1 = pilha.pop()

            if token == '+':
                pilha.append(valor1 + valor2)
            elif token == '-':
                pilha.append(valor1 - valor2)
            elif token == '*':
                pilha.append(valor1 * valor2)
            elif token == '/':
                pilha.append(valor1 / valor2)

    return int(pilha.pop())

def receber_entradas():
    lista_de_listas = []
    
    while True:
        entrada = input()
        
        if entrada == "Todas as expressoes foram enviadas!":
            break
        
        lista = []
        lista.append(entrada)
        
        while True:
            entrada = input()
            
            if entrada == "":
                break
                
            lista.append(entrada)
        
        lista_de_listas.append(lista)
    
    return lista_de_listas

def decodifica_binario(lista_de_listas):
    resultado = ""
    primeira_vez = True
    for lista in lista_de_listas:
        if not primeira_vez:
            resultado += " "
        primeira_vez = False
        for expressao in lista:
            expressao_resolvida = resolve_expressao(expressao)
            resultado += "1" if eh_numero_perfeito(expressao_resolvida) else "0"

    resultados = resultado.split(" ")
    return resultados

def decodifica_ascii(lista_de_binarios):
    palavra = ""
    for item in lista_de_binarios:
        palavra += chr(int(item, 2))
    return palavra
    
entradas = receber_entradas()
lista_de_binarios = decodifica_binario(entradas)
palavra = decodifica_ascii(lista_de_binarios)

for n in range(len(lista_de_binarios)):
    print(f"O {n + 1}º conjunto de expressoes resultou no binario {lista_de_binarios[n]} que em ASCII eh: {palavra[n]}\n")

print("A decodificacao final resultou em:")
print(f"{palavra}")



