def inicializa_lista(n):
    lista = []
    for index in range(n):
        lista.append(0)
    return lista

def extrair_numeros_da_entrada(entrada):
    partes = entrada.split(':')
    coeficiente = int(partes[0].split()[-1])
    numero = int(partes[1].strip())
    return coeficiente, numero

def calcula_derivada_de_ordem(coeficientes, n):
    if n >= len(coeficientes):
        return[0]

    if n == 0:
        return coeficientes
    
    derivada_coeficientes = []
    for i in range(1, len(coeficientes)):
        derivada_coeficientes.append(i * coeficientes[i])
    
    return calcula_derivada_de_ordem(derivada_coeficientes, n - 1)

def transforma_para_FPB(coeficientes):
    if all(item == 0 for item in coeficientes) or coeficientes == []:
        return "0"

    expoente = 0
    polinomio = ""
    for coeficiente in coeficientes:
        if coeficiente > 0:
            if coeficiente != 1:
                if expoente == 0:
                    polinomio += f"{coeficiente}"
                elif expoente == 1:
                    if polinomio != "":
                        polinomio += f"+{coeficiente}x"
                    else:
                        polinomio += f"{coeficiente}x"
                else:
                    if polinomio != "":
                        polinomio += f"+{coeficiente}x^{expoente}"
                    else:
                        polinomio += f"{coeficiente}x^{expoente}"
            else:
                if expoente == 0:
                    polinomio += f"{coeficiente}"
                elif expoente == 1:
                    if polinomio != "":
                        polinomio += f"+x"
                    else:
                        polinomio += f"x"
                else:
                    if polinomio != "":
                        polinomio += f"+x^{expoente}"
                    else:
                        polinomio += f"x^{expoente}"
        elif coeficiente < 0:
            if coeficiente != -1:
                if expoente == 0:
                    polinomio += f"{coeficiente}"
                elif expoente == 1:
                    polinomio += f"{coeficiente}x"
                else:
                    polinomio += f"{coeficiente}x^{expoente}"
            else:
                if expoente == 0:
                    polinomio += f"{coeficiente}"
                elif expoente == 1:
                    polinomio += f"-x"
                else:
                    polinomio += f"-x^{expoente}"
        expoente += 1
    return polinomio


grau_do_polinomio = int(input())
ordem_da_derivada = int(input())
qtd_coeficientes = int(input())

coeficientes = inicializa_lista(grau_do_polinomio + 1)

for _ in range(qtd_coeficientes):
    coeficiente, numero = extrair_numeros_da_entrada(input())
    coeficientes[coeficiente] = numero

derivada_coeficientes = calcula_derivada_de_ordem(coeficientes, ordem_da_derivada)

print(f"A derivada {ordem_da_derivada} do polinômio {transforma_para_FPB(coeficientes)} é")
print(f"{transforma_para_FPB(derivada_coeficientes)}")


