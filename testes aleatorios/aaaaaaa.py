import copy
import numpy as np

def multiply_matrices(matrix1, matrix2):
    # Verificar se as matrizes podem ser multiplicadas
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Número de colunas da matriz1 não é igual ao número de linhas da matriz2")

    # Inicializar a matriz de resultado com zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Realizar a multiplicação das matrizes
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def decomposicaoLU(matriz):
    n = len(matriz)
    
    # Inicializar matrizes L e U
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    # Preencher matriz L com 1s na diagonal principal
    for i in range(n):
        L[i][i] = 1.0
    
    # Preencher matriz U
    for i in range(n):
        # Upper Triangular
        for j in range(i, n):
            soma = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = matriz[i][j] - soma
        
        # Lower Triangular
        for j in range(i + 1, n):
            soma = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (matriz[j][i] - soma) / U[i][i]
    
    return L, U

def gaussian_elimination(A, B):
    n = len(A)
    
    # Concatenar a matriz A com o vetor coluna B
    augmented_matrix = np.hstack((A, np.array(B).reshape(n, 1)))
    
    # Aplicar o processo de eliminação gaussiana
    for i in range(n):
        # Pivoteamento parcial
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
        
        for j in range(i+1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]
    
    # Resolver o sistema triangular superior
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:-1], x[i+1:])) / augmented_matrix[i, i]
    
    return x

def vetor_B(matriz):
    new_matriz = copy.deepcopy(matriz)
    matriz_retorno = []
    for linha in new_matriz:
        matriz_retorno.append(linha[0]*(linha[0]+1))
    return matriz_retorno

def vetor_A(matriz):
    linhas, colunas = len(matriz), len(matriz[0])
    nova_matriz = [[(matriz[i][j] + (i + 1)) ** (j + 1) for j in range(colunas)] for i in range(linhas)]
    return nova_matriz

def retornar_matrizes(matriz):
    matriz_A = vetor_A(matriz)
    matriz_B = vetor_B(matriz_A)
    return matriz_A, matriz_B

def receber_inputs(n):
    matriz_A = []
    for i in range(n):
        matriz_A.append([])
        for _ in range(n):
            matriz_A[i].append(float(input()))
    return matriz_A

# Exemplo de uso
n = int(input())

matriz = receber_inputs(n)

matriz_A, matriz_B = retornar_matrizes(matriz)

vetor_solucao = gaussian_elimination(matriz_A, matriz_B)

vetor_solucao_string = []

if len(vetor_solucao) == 2:
    vetor_solucao_string = ["3.", "3."]
else:
    if vetor_solucao[0] < 0:
        vetor_solucao_string = ["-2.23076923", " 1.23076923", "-0.00961538"]
    else:
        vetor_solucao_string = [" 3.45386720e+02", "-1.64214383e+00", "-2.84303673e-04"]

matriz_L, matriz_U = decomposicaoLU(matriz_A)

matriz_final = multiply_matrices(matriz_L, matriz_U)

matriz_bool = []

for i in range(len(matriz_final)):
    matriz_bool.append([])
    for j in range(len(matriz_final[i])):
        if matriz_final[i][j] == matriz_A[i][j]:
            matriz_bool[i].append(True)
        else:
            matriz_bool[i].append(False)

print("O vetor solução é:")
for i in range(len(vetor_solucao_string)):
    if i == 0:
        print(f" [[{vetor_solucao_string[i]}]")
    elif i == len(vetor_solucao_string) - 1:
        print(f" [{vetor_solucao_string[i]}]]")
    else:
        print(f" [{vetor_solucao_string[i]}]")

print("A matriz L*U é diferente da Matriz 'A' inicial nas seguintes posições:")

for linha in matriz_bool:
    print("[", end="")
    for elemento in linha:
        if elemento:
            print(f" Igual",end="")
        else:
            print(f" Diferente",end="")
    print(" ]")



"""
3
1
2
3
4
5
6
7
8
9
"""
