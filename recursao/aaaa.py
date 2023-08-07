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

        

# Caso 1: Coeficientes vazios
print(transforma_para_FPB([]))  # Saída esperada: "0"

# Caso 2: Coeficientes contendo apenas zeros
print(transforma_para_FPB([0, 0, 0]))  # Saída esperada: "0"

# Caso 3: Coeficientes [1, 0, -3, 0, 2]
print(transforma_para_FPB([1, 0, -3, 0, 2]))  # Saída esperada: "x^4-3x^2+2"

# Caso 4: Coeficientes [2, -1, 0, 1]
print(transforma_para_FPB([2, -1, 0, 1]))  # Saída esperada: "2x^3-x^2+x"

# Caso 5: Coeficientes [-1, -1, -1, -1]
print(transforma_para_FPB([-1, -1, -1, -1]))  # Saída esperada: "-x^3-x^2-x"

# Caso 6: Coeficientes [0, 2, 0, -4, 5]
print(transforma_para_FPB([0, 2, 0, -4, 5]))  # Saída esperada: "2x^3-4x^2+5"

# Caso 7: Coeficientes [1, 2, 3, 4, 5]
print(transforma_para_FPB([1, 2, 3, 4, 5]))  # Saída esperada: "x^4+2x^3+3x^2+4x+5"
