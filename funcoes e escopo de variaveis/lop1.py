def is_row_dominant(matrix):
    n = len(matrix)
    
    for i in range(n):
        row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        diagonal = abs(matrix[i][i])
        
        if diagonal <= row_sum:
            return False, i  # A linha i não é dominante por linhas
    
    return True, None  # A matriz é dominante por linhas

def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def find_row_swaps_for_dominance(matrix):
    n = len(matrix)
    swaps = []
    
    for i in range(n):
        for j in range(i + 1, n):
            temp_matrix = [row[:] for row in matrix]
            swap_rows(temp_matrix, i, j)
            
            is_dominant, _ = is_row_dominant(temp_matrix)
            if is_dominant:
                swaps.append((i, j))
    
    return swaps

# Exemplo de uso
matrix = [
    [4, 1, -1],
    [1, 3, 2],
    [0, 5, 4]
]

dominant, problematic_row = is_row_dominant(matrix)

if dominant:
    print("A matriz é dominante por linhas.")
else:
    print(f"A matriz não é dominante por linhas. Trocar a linha {problematic_row} pode melhorar a dominância.")

possible_swaps = find_row_swaps_for_dominance(matrix)
if possible_swaps:
    print("Trocas que podem melhorar a dominância:")
    for swap in possible_swaps:
        print(f"Trocar linha {swap[0]} com linha {swap[1]}")
else:
    print("Não foram encontradas trocas que possam melhorar a dominância.")





