
import numpy as np

def jacobi_method(A, b, initial_guess=None, min_error=1e-10, max_error=1e4, max_iterations=100):
    n = len(b)
    
    if initial_guess is None:
        x_k = np.zeros(n)
    else:
        x_k = np.array(initial_guess)
    
    x_k1 = np.zeros(n)
    iteration = 0
    error = min_error + 1  # Initialize error to be greater than max_error
    
    while error > min_error and error < max_error and iteration < max_iterations:
        for i in range(n):
            sum_term = sum(A[i][j] * x_k[j] for j in range(n) if j != i)
            x_k1[i] = (b[i] - sum_term) / A[i][i]
        
        error = np.sqrt(sum((1 - x_k1[i])**2 for i in range(n)))
        x_k = x_k1.copy()
        iteration += 1
    
    return x_k, iteration, error

def gauss_seidel_method(A, b, initial_guess=None, min_error=1e-10, max_error=1e4, max_iterations=1000):
    n = len(b)
    
    if initial_guess is None:
        x_k = np.zeros(n)
    else:
        x_k = np.array(initial_guess)
    
    x_k1 = np.zeros(n)
    iteration = 0
    error = min_error + 1  # Initialize error to be greater than max_error
    
    while error > min_error and error < max_error and iteration < max_iterations:
        for i in range(n):
            sum_term1 = sum(A[i][j] * x_k1[j] for j in range(i))
            sum_term2 = sum(A[i][j] * x_k[j] for j in range(i + 1, n))
            x_k1[i] = (b[i] - sum_term1 - sum_term2) / A[i][i]
        
        error = np.sqrt(sum((1 - x_k1[i])**2 for i in range(n)))
        x_k = x_k1.copy()
        iteration += 1
    
    return x_k, iteration, error

def recebe_valores(n):
    A = []
    for i in range(n):
        A.append([])
        for _ in range(n):
            A[i].append(float(input()))
    b = []
    for _ in range(n):
        b.append(float(input()))
    
    input()
    input()
    return A, b

# Exemplo de uso
n = int(input())

A, b = recebe_valores(n)

solution_jacobi, num_int_jacobi, erro_jacobi = jacobi_method(A, b)
solution_gauss, num_int_gauss, erro_gauss = gauss_seidel_method(A, b)

for i in range(0,n):
 	print("Jacobi: ",round(solution_jacobi[i],10))
print("Jacobi: ", num_int_jacobi,"\nJacobi: ", round(erro_jacobi,10))

for i in range(0,n):
 	print("Gauss-seidel: ",round(solution_gauss[i],10))
print("Gauss-seidel: ", num_int_gauss,"\nGauss-seidel: ", round(erro_gauss,10))
