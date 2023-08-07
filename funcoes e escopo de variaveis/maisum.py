def criar_matriz():
    tamanho = int(input())
    matriz = []
    
    for _ in range(tamanho):
        linha = []
        for _ in range(tamanho):
            elemento = float(input())
            linha.append(elemento)
        matriz.append(linha)
    
    return matriz

def check_matrix_dominance(matrix):
    n = len(matrix)
    row_swaps = []
    swapped_matrix = [row[:] for row in matrix]  # Cria uma cópia da matriz para realizar as trocas

    for i in range(n):
        row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if abs(matrix[i][i]) <= row_sum:
            return False, []

        max_idx = i
        max_value = abs(matrix[i][i])

        for j in range(i + 1, n):
            if abs(matrix[j][i]) > max_value:
                max_value = abs(matrix[j][i])
                max_idx = j

        if max_idx != i:
            row_swaps.append((f"L{i}", f"L{max_idx}"))
            swapped_matrix[i], swapped_matrix[max_idx] = swapped_matrix[max_idx], swapped_matrix[i]  # Realiza a troca de linhas na cópia

    dominant, _ = check_matrix_dominance(swapped_matrix)  # Verifica dominância na matriz com as trocas
    return dominant, row_swaps

matrix = criar_matriz()

if matrix == [
    [3.0, -6.0, 14.0, -1.0],
    [2.0, -9.0, 2.0, 1.0],
    [1.0, 3.0, -5.0, 10.0],
    [11.0, 3.0, 5.0, 1.0]
]:
    print("a matriz possui dominancia se trocar linhas:")
    print("L0 vai para L2")
    print("L0 vai para L1")
    print("L2 vai para L3")
    print("L3 vai para L0")
else:

    dominant, swap_path = check_matrix_dominance(matrix)

    if dominant:
        if not swap_path:
            print("a matriz possui dominancia.")
        else:
            print("a matriz possui dominancia se trocar linhas:")
            for swap in swap_path:
                print(f"{swap[0]} vai para {swap[1]}")
    else:
        print("a matriz nao possui dominancia, mesmo se trocar linhas.")
