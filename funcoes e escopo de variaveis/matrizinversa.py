import numpy as np

def norm_inf(matrix):
    return np.max(np.sum(np.abs(matrix), axis=1))

def matrix_condition_number(matrix, inv_matrix):
    norm_A = norm_inf(matrix)
    norm_inv_A = norm_inf(inv_matrix)
    
    condition_number = norm_A * norm_inv_A
    return condition_number

def imprimir_matriz(matriz):
    for linha in matriz:
        linha_formatada = " ".join([f"{numero:.2f}" for numero in linha])
        print(linha_formatada)

def criar_matriz():
    tamanho = int(input())
    matriz = []

    for _ in range(tamanho):
        linha = []
        for _ in range(tamanho):
            coeficiente = float(input())
            linha.append(coeficiente)
        matriz.append(linha)

    vetor_b = []
    for _ in range(tamanho):
        termo_b = float(input())
        vetor_b.append(termo_b)

    matriz_completa = []
    for i in range(tamanho):
        linha_completa = matriz[i] + [vetor_b[i]]
        matriz_completa.append(linha_completa)

    return matriz_completa

def arredondar_matriz(matriz):
    matriz_arredondada = []
    
    for linha in matriz:
        linha_arredondada = [round(numero, 2) for numero in linha]
        matriz_arredondada.append(linha_arredondada)
    
    return matriz_arredondada

def remover_ultima_coluna(matriz):
    nova_matriz = []
    for linha in matriz:
        nova_linha = linha[:-1]  # Remove o último elemento da linha
        nova_matriz.append(nova_linha)
    return nova_matriz


def gauss_jordan_inverse(matrix):
    n = len(matrix)
    
    # Criar a matriz aumentada [matrix | identidade]
    augmented_matrix = np.hstack((matrix, np.identity(n)))
    
    # Aplicar Gauss-Jordan para transformar a parte esquerda da matriz aumentada em uma matriz identidade
    for col in range(n):
        # Dividir a linha pelo pivô
        pivot = augmented_matrix[col][col]
        augmented_matrix[col] /= pivot
        
        # Subtrair múltiplos da linha atual das outras linhas para tornar os elementos abaixo e acima do pivô zero
        for row in range(n):
            if row != col:
                factor = augmented_matrix[row][col]
                augmented_matrix[row] -= factor * augmented_matrix[col]
    
    # A parte direita da matriz aumentada agora contém a inversa da matriz original
    inverse_matrix = augmented_matrix[:, n:]
    
    return inverse_matrix

def calcular_e_printar_raizes(matriz_original):
    matriz_original = np.array(matriz_original)
    nova_matriz = remover_ultima_coluna(matriz_original)
    inversa = gauss_jordan_inverse(nova_matriz)
    b = matriz_original[:, -1]  # Vetor coluna dos termos independentes
    
    n = len(inversa)
    raizes = []

    for i in range(n):
        raiz = 0
        for j in range(n):
            raiz += inversa[i][j] * b[j]
        raizes.append(raiz)
        print(f'x{i} {raiz:.2f}')

# Exemplo de uso
matriz_original = criar_matriz()
matriz_original = np.array(matriz_original)

nova_matriz = remover_ultima_coluna(matriz_original)
inversa = gauss_jordan_inverse(nova_matriz)
inversa_arredondada = arredondar_matriz(inversa)

print("A matriz inversa de A é:\n")
imprimir_matriz(inversa_arredondada)
print("")

numero_de_condicionamento = round(matrix_condition_number(nova_matriz, inversa), 2)
print(f"O número de condição é {numero_de_condicionamento}")
if numero_de_condicionamento > 1000:
    print("Há indícios de mal-condicionamento")
else:
    print("Não há indícios de mal-condicionamento")

print("")
calcular_e_printar_raizes(matriz_original)




